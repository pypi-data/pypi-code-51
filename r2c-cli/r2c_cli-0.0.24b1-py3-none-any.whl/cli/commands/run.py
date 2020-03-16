import json
import os
from typing import List, Optional, Union

import click

from r2c.cli.commands.cli import cli
from r2c.cli.logger import (
    abort_on_build_failure,
    get_logger,
    print_error_exit,
    print_exception_exit,
    print_msg,
    print_success,
    print_warning,
)
from r2c.cli.network import (
    docker_login,
    get_base_url,
    get_docker_creds,
    get_registry_data,
)
from r2c.cli.run import build_docker, pull_docker, run_analyzer_on_local_code
from r2c.cli.util import (
    find_and_open_analyzer_manifest,
    load_params,
    parse_remaining,
    set_debug_flag,
    set_verbose_flag,
)
from r2c.lib.analysis import AnalyzerNonZeroExitError
from r2c.lib.analyzer import AnalyzerName, VersionedAnalyzer
from r2c.lib.errors import AnalyzerOutputNotFound, SymlinkNeedsElevationError
from r2c.lib.input import AnalyzerInput, LocalCode

logger = get_logger()


# Hack click to accepting optional options
# https://stackoverflow.com/questions/40753999/python-click-make-option-value-optional
class InteractiveOption(click.Option):
    pass


class InteractiveNameOption(click.Option):
    def get_help_record(self, ctx):
        """ Fix the help text to eliminate  _name suffix """
        cmd_help = super().get_help_record(ctx)
        # replace _name from help menu, rest of the menu stays the same
        update_cmd_help = cmd_help[0].replace("_name", "=").replace(" ", "")
        return (update_cmd_help,) + cmd_help[1:]


class InteractiveCommand(click.Command):
    def parse_args(self, ctx, args):
        interactive_options: List = []
        for option in ctx.command.params:
            if isinstance(option, InteractiveOption):
                interactive_options = option.opts

        # only for InteractiveOption, rewrite the option so that InteractiveNameOption can pick it up
        for i, arg in enumerate(args):
            arg = arg.split("=")
            # if InteractiveOption was specified with arguments
            if arg[0] in interactive_options and len(arg) > 1:
                arg[0] += "_name"
                args[i] = "=".join(arg)

        return super().parse_args(ctx, args)


@cli.command(cls=InteractiveCommand)
@click.argument("code_dir")
@click.option(
    "-A",
    "--analyzer-directory",
    default=os.getcwd(),
    help="The directory where the analyzer is located, defaulting to the current directory.",
)
@click.option(
    "-a", "--analyzer", help="Name of the analyzer: e.g. `r2c/js-permissions`"
)
@click.option("--version", help="Version of the analyzer: e.g. `0.0.1`")
@click.option("-o", "--output-path", help="Output path for analyzer's output json")
@click.option(
    "-q",
    "--quiet",
    is_flag=True,
    default=False,
    help="Don't print analyzer output to stdout after it completes",
)
@click.option(
    "--analyzer-quiet",
    is_flag=True,
    default=False,
    help="Don't print analyzer logging to stdout or stderr while it runs",
)
@click.option(
    "--no-login",
    is_flag=True,
    default=False,
    help="Do not run `docker login` command during run.",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Show extra output, error messages, and exception stack traces with INFO filtering",
    default=False,
)
@click.option(
    "--debug",
    "-d",
    is_flag=True,
    help="Show extra output, error messages, and exception stack traces with DEBUG filtering",
    default=False,
    hidden=True,
)
@click.option(
    "--input-json",
    hidden=True,
    is_flag=True,
    help="If set, the code_dir argument is interpreted as a JSON-serialized r2c.lib.input.AnalyzerInput. This means you can actually run analyzers like public/pypi locally.",
)
@click.option(
    "--interactive",
    "-i",
    is_flag=True,
    cls=InteractiveOption,
    default=False,
    help="Shell into last docker container in the execution chain.",
)
@click.option(
    "--interactive_name",
    "-i_name",
    cls=InteractiveNameOption,
    type=str,
    default=None,
    help="Shell into docker container via `docker exec -it` by analyzer name. If multiple analyzer match, shells into the first container in the execution chain.",
)
@click.option(
    "--reset-cache",
    is_flag=True,
    default=False,
    show_default=True,
    help="Resets local cache.",
)
@click.option(
    "--parameters",
    default="{}",
    help='Parameters to pass to the top level analyzer being run, as a JSON object. If not specified, an empty object will be passed. The meaning of the parameters depends on the individual analyzer. If your parameters are stored in a file, you can use something like "$(cat /path/to/file)".',
)
@click.option(
    "--run-as-host-uid",
    is_flag=True,
    default=False,
    help="If true, the analyzer is run using the same UID as the Docker host. This saves a second or two on analyzer execution, but can potentially run into issues with some analyzers that set overly-restrictive permissions on files inside their container. If you run into an analyzer that this doesn't work with, please let us (or the author) know.",
)
@click.argument("env-args-string", nargs=-1, type=click.Path())
@click.pass_context
def run(
    ctx,
    analyzer_directory,
    analyzer,
    version,
    code_dir,
    output_path,
    quiet,
    analyzer_quiet,
    no_login,
    debug,
    input_json,
    interactive,
    interactive_name,
    reset_cache,
    verbose,
    parameters,
    run_as_host_uid,
    env_args_string,
):
    """
    Run the analyzer in the current directory over a code directory.

    You may have to log in if your analyzer depends on privately
    published analyzers.
    """

    if verbose is True:  # allow passing --verbose to run as well as globally
        set_verbose_flag(ctx, True)
    if debug is True:
        set_debug_flag(ctx, True)
    print_msg(f"🏃 Starting to run analyzer...")

    env_args_dict = parse_remaining(env_args_string)

    parameter_obj = load_params(parameters)

    registry_data = get_registry_data()

    if analyzer:
        version_str = version if version else "*"
        resolved_version = registry_data._resolve(AnalyzerName(analyzer), version_str)
        if resolved_version:
            va = VersionedAnalyzer(AnalyzerName(analyzer), resolved_version)
            manifest = registry_data.manifest_for(va)
        else:
            print_error_exit(f"Could not resolve the version for {analyzer}")
    else:
        manifest, analyzer_directory = find_and_open_analyzer_manifest(
            analyzer_directory, ctx
        )

    dependencies = manifest.dependencies
    print_msg("Resolving dependencies")
    logger.debug(f"Parsing and resolving dependencies: {dependencies}")
    if dependencies:
        for analyzer_dep in dependencies:
            dep_name = analyzer_dep.name
            dep_semver_version = analyzer_dep.wildcard_version
            dep_version = registry_data._resolve(
                AnalyzerName(analyzer_dep.name), dep_semver_version
            )
            if not dep_version:
                if not analyzer_dep.path:
                    print_error_exit(
                        f"Error resolving dependency {dep_name} at version {dep_semver_version}. Check that you're using the right version of this dependency and try again."
                    )
            logger.debug(f"Resolved dependency {dep_name}:{dep_semver_version}")

        if not no_login:
            # we need at least one dep and its version to get credentials when the user isn't logged in
            dep_name = dependencies[0].name
            dep_semver_version = dependencies[0].wildcard_version
            dep_version = registry_data._resolve(
                AnalyzerName(dep_name), dep_semver_version
            )

            artifact_link = (
                f"{get_base_url()}/api/v1/artifacts/{dep_name}/{dep_version}"
            )
            logger.debug(f"Getting credential from {artifact_link}")

            # TODO (ulzii) use proper auth credential once its done
            creds = get_docker_creds(artifact_link)
            if creds is None:
                print_error_exit(
                    "Error getting dependency credentials. Please contact us with the following information: failed to get Docker credentials."
                )
            # docker login
            successful_login = docker_login(creds)
            if not successful_login:
                print_error_exit(
                    "Error validating dependency credentials. Please contact us with the following information: failed to log in to Docker."
                )
    else:
        print_warning(
            "No dependencies found; are dependencies intentionally omitted in analyzer.json? Most analyzers are expected to have 1 or more dependencies (e.g. for taking source code as input)."
        )
    print_msg("🔨 Building docker container")

    if not analyzer:
        abort_on_build_failure(
            build_docker(
                manifest.analyzer_name,
                manifest.version,
                os.path.relpath(analyzer_directory, os.getcwd()),
                env_args_dict=env_args_dict,
                no_cache=reset_cache,
            )
        )
    else:
        print_msg(f"🔨 Pulling docker image for {va.name}")
        abort_on_build_failure(pull_docker(va))

    if input_json:
        analyzer_input = AnalyzerInput.from_json(json.loads(code_dir))
    else:
        analyzer_input = LocalCode(code_dir)

    try:
        interactive_selector: Optional[Union[int, str]] = None
        if interactive:
            print_msg(
                f"🔎 Inspecting containers interactively by `docker exec` into last analyzer in execution."
            )
            interactive_selector = -1
        elif interactive_name:
            print_msg(
                f"🔎 Inspecting containers interactively by `docker exec` into analyzer with name containing `{interactive_name}`."
            )
            interactive_selector = interactive_name
        else:
            print_msg(f"🔎 Running analysis on `{analyzer_input}`")

        logger.info(f"Reset cache: {reset_cache}")
        try:
            run_analyzer_on_local_code(
                registry_data=registry_data,
                manifest=manifest,
                analyzer_dir=analyzer_directory,
                analyzer_input=analyzer_input,
                output_path=output_path,
                show_output_on_stdout=not quiet,
                pass_analyzer_output=not analyzer_quiet,
                parameters=parameter_obj,
                env_args_dict=env_args_dict,
                interactive=interactive_selector,
                run_as_host_uid=run_as_host_uid,
                reset_cache=reset_cache,
            )
        except AnalyzerOutputNotFound as fne:
            print_error_exit(str(fne), err=False)
        except AnalyzerNonZeroExitError as ae:
            print_exception_exit("Analyzer non-zero exit", ae, err=False)
        if output_path:
            path_msg = f"Analysis results in `{output_path}`."
        else:
            path_msg = f"Analysis results printed to `stdout`. unless suppressed explicitly with `-q`"
        print_success(f"Finished analyzing `{analyzer_input}`. {path_msg}")

    except SymlinkNeedsElevationError as sym:
        print_error_exit(
            f"Error setting up local analysis. {sym}. Try again as an admin."
        )
