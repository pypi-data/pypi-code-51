# -*- coding: utf-8 -*-
"""
AS3 Ninja CLI module
"""

# pylint: disable=C0330 # Wrong hanging indentation before block
# pylint: disable=C0301 # Line too long

import json
import sys
from typing import Optional, Union

import click
from loguru import logger

from . import __version__
from .declaration import AS3Declaration
from .gitget import Gitget
from .schema import AS3Schema
from .templateconfiguration import AS3TemplateConfiguration
from .utils import deserialize, failOnException

logger.remove()
LOG_STDERR = logger.bind(task="stderr")
LOG_STDOUT = logger.bind(task="stdout")
logger.add(
    sys.stderr,
    colorize=True,
    format="<red>{level}: {message}</red>",
    filter=lambda record: record["extra"]["task"] == "stderr",
)
logger.add(
    sys.stdout,
    colorize=True,
    format="<blue>{level}:</blue> <green>{message}</green>",
    filter=lambda record: record["extra"]["task"] == "stdout",
)


def _output_declaration(
    as3declaration: AS3Declaration, output_file: Union[str, None], pretty: bool,
):
    """
    Function to output the transformed declaration
    """
    if output_file:
        output_file.write(as3declaration.json())
    else:
        if pretty:
            print(json.dumps(as3declaration.dict(), indent=4, sort_keys=True))
        else:
            print(as3declaration.json())


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(version=__version__)
def cli() -> None:
    """main cli command group"""


@cli.command()
@click.option(
    "-t",
    "--declaration-template",
    required=False,
    type=click.File("r"),
    help="Declaration Template file used for transformation (Jinja2 producing JSON)",
)
@click.option(
    "-c",
    "--configuration-file",
    required=False,
    nargs=0,
    type=click.Path(),
    help="Template Configuration file(s) to parameterize the Declaration Template (multiple files allowed)",
)
@click.argument("configuration-file", nargs=-1)
@click.option(
    "-o",
    "--output-file",
    required=False,
    type=click.File("w"),
    help="Output file, STDOUT is used otherwise",
)
@click.option(
    "--validate/--no-validate",
    required=False,
    default=True,
    is_flag=True,
    help="Validate/do not validate the generated AS3 Declaration against the AS3 JSON Schema (validate is the default)",
)
@click.option(
    "--pretty",
    required=False,
    default=False,
    is_flag=True,
    help="Pretty print JSON (when printed to STDOUT)",
)
@failOnException
@LOG_STDERR.catch(reraise=True)
def transform(
    declaration_template: str,
    configuration_file: Optional[tuple],
    output_file: Union[str, None],
    validate: bool,  # pylint: disable=W0621 # Redefining name 'validate' from outer scope
    pretty: bool,
):
    """Render AS3 Declaration from local files.

    Transforms a Declaration Template using the Template Configuration file(s) to an AS3 Delcaration.

    It is then validated against the AS3 JSON Schema unless validation is disabled.

    If no Declaration Template is specified, it is read from the Template Configuration (as3ninja.declaration_template).
    If no Template Configuration is specified, the first default configuration file (ninja.json, ninja.yaml, ninja.yml). The file is expected to be in the CWD.
    """
    template = None
    if declaration_template:
        template = declaration_template.read()

    as3tc = AS3TemplateConfiguration(template_configuration=configuration_file)
    as3declaration = AS3Declaration(
        declaration_template=template, template_configuration=as3tc.dict()
    )

    if validate:
        as3s = AS3Schema()
        as3s.validate(declaration=as3declaration.dict())

    _output_declaration(as3declaration, output_file=output_file, pretty=pretty)


@cli.command()
@click.option(
    "-t",
    "--declaration-template",
    required=False,
    type=click.Path(),
    help="Declaration Template file used for transformation (Jinja2 producing JSON)",
)
@click.option(
    "-c",
    "--configuration-file",
    required=False,
    nargs=0,
    type=click.Path(),
    help="Template Configuration file(s) to parameterize the Declaration Template (multiple files allowed)",
)
@click.argument("configuration-file", nargs=-1)
@click.option(
    "-o",
    "--output-file",
    required=False,
    type=click.File("w"),
    help="Output file, STDOUT is used otherwise",
)
@click.option(
    "--validate/--no-validate",
    required=False,
    default=True,
    is_flag=True,
    help="Validate/do not validate the generated AS3 Declaration against the AS3 JSON Schema (validate is the default)",
)
@click.option(
    "--pretty",
    required=False,
    default=False,
    is_flag=True,
    help="Pretty print JSON (when printed to STDOUT)",
)
@click.option("--repository", required=True, default=False, help="Git repository")
@click.option("--branch", required=False, default=False, help="Git branch to use")
@click.option(
    "--commit", required=False, default=False, help="Git commit id or HEAD~<int>"
)
@click.option("--depth", required=False, default=False, help="Git clone depth")
@failOnException
@LOG_STDERR.catch(reraise=True)
def git_transform(  # pylint: disable=R0913 # Too many arguments
    declaration_template: Optional[str],
    configuration_file: Optional[tuple],
    output_file: Union[str, None],
    validate: bool,  # pylint: disable=W0621 # Redefining name 'validate' from outer scope
    pretty: bool,
    repository: str,
    branch: Union[str, None],
    commit: Union[str, None],
    depth: Union[int, None],
):
    """Render AS3 Declaration from Git Repository.

    Clones the Git repository with the specified options and then transforms the Declaration Template using the Template Configuration file(s) to an AS3 Delcaration.

    It is then validated against the AS3 JSON Schema unless validation is disabled.

    If no Declaration Template is specified, it is read from the Template Configuration (as3ninja.declaration_template).
    If no Template Configuration is specified, the first default configuration file (ninja.json, ninja.yaml, ninja.yml). The file is expected to be in the root of the Git repository.
    """
    with Gitget(
        repository=repository, branch=branch, commit=commit, depth=depth
    ) as gitrepo:
        as3tc = AS3TemplateConfiguration(
            template_configuration=configuration_file,
            base_path=f"{gitrepo.repodir}/",
            overlay={"as3ninja": {"git": gitrepo.info}},
        )

        if declaration_template is not None:
            with open(f"{gitrepo.repodir}/{declaration_template}", "r") as template:
                declaration_template = template.read()

        as3declaration = AS3Declaration(
            template_configuration=as3tc.dict(),
            declaration_template=declaration_template,
            jinja2_searchpath=gitrepo.repodir,
        )
        if validate:
            as3s = AS3Schema()
            as3s.validate(declaration=as3declaration.dict())

        _output_declaration(as3declaration, output_file=output_file, pretty=pretty)


@cli.command()
@click.option(
    "-d",
    "--declaration",
    required=False,
    type=click.File("r"),
    help="AS3 Declaration file (JSON) to validate",
)
@click.option(
    "-v",
    "--version",
    required=False,
    default="latest",
    help="AS3 Schema version to use for validation (e.g. 3.16.0)",
)
@failOnException
@LOG_STDERR.catch(reraise=True)
def validate(
    declaration: str, version: Optional[str],
):
    """Validate an AS3 Declaration against the AS3 JSON Schema.

    If no version is specified, the latest available version is used."""
    as3s = AS3Schema(version=version)
    _declaration = deserialize(declaration.name)
    as3s.validate(declaration=_declaration)
    LOG_STDOUT.info(
        "Validation passed for AS3 Schema version: {}",
        as3s.version,
        feature="f-strings",
    )
