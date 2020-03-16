#
#    Copyright 2019 EPAM Systems
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
import http

import click
from odahuflow.cli.utils.client import pass_obj
from odahuflow.cli.utils.error_handler import ID_AND_FILE_MISSED_ERROR_MESSAGE, \
    IGNORE_NOT_FOUND_ERROR_MESSAGE
from odahuflow.cli.utils.output import format_output, DEFAULT_OUTPUT_FORMAT, validate_output_format
from odahuflow.sdk import config
from odahuflow.sdk.clients.connection import ConnectionClient
from odahuflow.sdk.clients.api import WrongHttpStatusCode
from odahuflow.sdk.clients.api_aggregated import parse_resources_file_with_one_item
from odahuflow.sdk.models import Connection


@click.group()
@click.option('--url', help='API server host', default=config.API_URL)
@click.option('--token', help='API server jwt token', default=config.API_TOKEN)
@click.pass_context
def connection(ctx: click.core.Context, url: str, token: str):
    """
    Allow you to perform actions on connections.\n
    Alias for the command is conn.
    """
    ctx.obj = ConnectionClient(url, token)


@connection.command()
@click.option('--conn-id', '--id', help='Connection ID')
@click.option('--output-format', '-o', 'output_format', help='Output format',
              default=DEFAULT_OUTPUT_FORMAT, callback=validate_output_format)
@click.option('--decrypted', '-d', help='Flag means that connection sensitive data should be decrypted',
              default=False, is_flag=True)
@pass_obj
def get(client: ConnectionClient, conn_id: str, output_format: str, decrypted: bool):
    """
    Get connections.\n
    The command without id argument retrieve all connections.\n
    Get all connections in json format:\n
        odahuflowctl conn get --format json\n
    Get connection with "git-repo" id:\n
        odahuflowctl conn get --id git-repo\n
    Using jsonpath:\n
        odahuflowctl conn get -o 'jsonpath=[*].spec.reference'
    \f
    :param decrypted: if set than decrypted connection will be returned
    :param client: Connection HTTP client
    :param conn_id: Connection ID
    :param output_format: Output format
    :return:
    """
    if conn_id:
        if decrypted:
            conn = client.get_decrypted(conn_id)
        else:
            conn = client.get(conn_id)

        conns = [conn]
    else:
        conns = client.get_all()

    format_output(conns, output_format)


@connection.command()
@click.option('--conn-id', '--id', help='Connection ID')
@click.option('--file', '-f', type=click.Path(), required=True, help='Path to the file with connection')
@click.option('--output-format', '-o', 'output_format', help='Output format',
              default=DEFAULT_OUTPUT_FORMAT, callback=validate_output_format)
@pass_obj
def create(client: ConnectionClient, conn_id: str, file: str, output_format: str):
    """
    Create a connection.\n
    You should specify a path to file with a connection. The file must contain only one connection.
    For now, CLI supports yaml and JSON file formats.
    If you want to create multiples connections than you should use "odahuflowctl res apply" instead.
    If you provide the connection id parameter than it will be overridden before sending to API server.\n
    Usage example:\n
        * odahuflowctl conn create -f conn.yaml --id examples-git
    \f
    :param client: Connection HTTP client
    :param conn_id: Connection ID
    :param file: Path to the file with only one connection
    :param output_format: Output format
    """
    conn = parse_resources_file_with_one_item(file).resource
    if not isinstance(conn, Connection):
        raise ValueError(f'Connection expected, but {type(conn)} provided')

    if conn_id:
        conn.id = conn_id

    click.echo(format_output([client.create(conn)], output_format))


@connection.command()
@click.option('--conn-id', '--id', help='Connection ID')
@click.option('--file', '-f', type=click.Path(), required=True, help='Path to the file with connection')
@click.option('--output-format', '-o', 'output_format', help='Output format',
              default=DEFAULT_OUTPUT_FORMAT, callback=validate_output_format)
@pass_obj
def edit(client: ConnectionClient, conn_id: str, file: str, output_format: str):
    """
    Update a connection.\n
    You should specify a path to file with a connection. The file must contain only one connection.
    For now, CLI supports yaml and JSON file formats.
    If you want to update multiples connections than you should use "odahuflowctl res apply" instead.
    If you provide the connection id parameter than it will be overridden before sending to API server.\n
    Usage example:\n
        * odahuflowctl conn update -f conn.yaml --id examples-git
    \f
    :param client: Connection HTTP client
    :param conn_id: Connection ID
    :param file: Path to the file with only one connection
    :param output_format: Output format
    """
    conn = parse_resources_file_with_one_item(file).resource
    if not isinstance(conn, Connection):
        raise ValueError(f'Connection expected, but {type(conn)} provided')

    if conn_id:
        conn.id = conn_id

    click.echo(format_output([client.edit(conn)], output_format))


@connection.command()
@click.option('--conn-id', '--id', help='Connection ID')
@click.option('--file', '-f', type=click.Path(), help='Path to the file with connection')
@click.option('--ignore-not-found/--not-ignore-not-found', default=False,
              help='ignore if connection is not found')
@pass_obj
def delete(client: ConnectionClient, conn_id: str, file: str, ignore_not_found: bool):
    """
    Delete a connection.\n
    For this command, you must provide a connection ID or path to file with one connection.
    The file must contain only one connection.
    If you want to delete multiples connections than you should use "odahuflowctl res delete" instead.
    For now, CLI supports yaml and JSON file formats.
    The command will be failed if you provide both arguments.\n
    Usage example:\n
        * odahuflowctl conn delete --id examples-git\n
        * odahuflowctl conn delete -f conn.yaml\n
        * odahuflowctl conn delete --id examples-git --ignore-not-found
    \f
    :param client: Connection HTTP client
    :param conn_id: Connection ID
    :param file: Path to the file with only one connection
    :param ignore_not_found: ignore if connection is not found
    """
    if not conn_id and not file:
        raise ValueError(ID_AND_FILE_MISSED_ERROR_MESSAGE)

    if conn_id and file:
        raise ValueError(ID_AND_FILE_MISSED_ERROR_MESSAGE)

    if file:
        conn = parse_resources_file_with_one_item(file).resource
        if not isinstance(conn, Connection):
            raise ValueError(f'Connection expected, but {type(conn)} provided')

        conn_id = conn.id

    try:
        click.echo(client.delete(conn_id))
    except WrongHttpStatusCode as e:
        if e.status_code != http.HTTPStatus.NOT_FOUND or not ignore_not_found:
            raise e

        click.echo(IGNORE_NOT_FOUND_ERROR_MESSAGE.format(conn_id))
