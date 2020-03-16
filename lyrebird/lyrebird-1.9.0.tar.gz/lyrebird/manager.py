import argparse
import webbrowser
import json
import socket
import threading
import signal
import os
import resource
import traceback
from pathlib import Path
from lyrebird import log
from lyrebird import application
from lyrebird.config import Rescource, ConfigManager
from lyrebird.mock.mock_server import LyrebirdMockServer
from lyrebird.proxy.proxy_server import LyrebirdProxyServer
from lyrebird.event import EventServer
from lyrebird.task import BackgroundTaskServer
from lyrebird.notice_center import NoticeCenter
from lyrebird.db.database_server import LyrebirdDatabaseServer
from lyrebird.plugins import PluginManager
from lyrebird.checker import LyrebirdCheckerServer
from lyrebird import version
from lyrebird import reporter
from lyrebird import mock_data_tools
from lyrebird import project_builder
from packaging.version import parse as vparse


logger = log.get_logger()

MOCK_DATA_V_1_7_0 = vparse('1.7.0')
MOCK_DATA_V_1_0_0 = vparse('1.0.0')
MOCK_DATA_V_0_15_0 = vparse('0.15.0')


def main():
    """
    Command line main entry

    Start lyrebird

    * start in default config
    ```
    lyrebird
    ```
    * start with verbose mode
    ```
    lyrebird -v
    ```
    * start without open a web browser
    ```
    lyrebird -b
    ```
    * start with a specified config file
    ```
    lyrebird -c /path/to/your/config/file
    ```
    * start with multipart args
    ```
    lyrebird -v --mock 8080 -c /path/to/your/config/file
    ```
    """
    parser = argparse.ArgumentParser(prog='lyrebird')

    parser.add_argument('-V', '--version', dest='version', action='store_true', help='show lyrebird version')
    parser.add_argument('-v', dest='verbose', action='count', default=0, help='Show verbose log')
    parser.add_argument('--mock', dest='mock', type=int, help='Set mock server port, default port is 4272')
    parser.add_argument('--proxy', dest='proxy', type=int, help='Set proxy server port, default port is 9090')
    parser.add_argument('--data', dest='data', help='Set data dir, default is "./data/"')
    parser.add_argument('-b', '--no_browser', dest='no_browser',
                        action='store_true', help='Start without open a browser')
    parser.add_argument('-c', '--config', dest='config',
                        help='Start with a config file. Default is "~/.lyrebird/conf.json"')
    parser.add_argument('--log', dest='log', help='Set output log file path')
    parser.add_argument('--script', action='append', help='Set a checker script path')
    parser.add_argument('--plugin', action='append', help='Set a plugin project path')
    parser.add_argument('--database', dest='database', help='Set a database path. Default is "~/.lyrebird/lyrebird.db"')

    subparser = parser.add_subparsers(dest='sub_command')

    gen_parser = subparser.add_parser('gen')
    gen_parser.add_argument('path', help='Create plugin project')

    args = parser.parse_args()

    if args.version:
        print(version.LYREBIRD)
        return

    Path('~/.lyrebird').expanduser().mkdir(parents=True, exist_ok=True)

    if args.config:
        application._cm = ConfigManager(conf_path=args.config)
    else:
        application._cm = ConfigManager()

    # set current ip to config
    try:
        application._cm.config['ip'] = _get_ip()
    except socket.gaierror as e:
        logger.error('Failed to get local IP address, error occurs on %s' % e)

    # init file logger after config init
    application._cm.config['verbose'] = args.verbose
    log.init(args.log)

    if args.mock:
        application._cm.config['mock.port'] = args.mock
    if args.proxy:
        application._cm.config['proxy.port'] = args.proxy
    if args.data:
        application._cm.config['mock.data'] = args.data

    logger.debug(f'Read args: {args}')

    if args.sub_command == 'gen':
        logger.debug('EXEC: Plugin project generator')
        gen(args)
    else:
        logger.debug('EXEC: LYREBIRD START')
        run(args)


def run(args: argparse.Namespace):
    # Set file descriptors
    try:
        resource.setrlimit(resource.RLIMIT_NOFILE, (8192, 8192))
    except Exception:
        traceback.print_exc()
        logger.warning('Set file descriptors failed\nPlease set it by your self, use "ulimit -n 8192" with root account')
    # Check mock data group version. Update if is older than 1.x
    data_path = application._cm.config['mock.data']
    Path(data_path).mkdir(parents=True, exist_ok=True)
    res = mock_data_tools.check_data_version(data_path)
    mockdata_version = vparse(res)

    if MOCK_DATA_V_1_0_0 <= mockdata_version < MOCK_DATA_V_1_7_0:
        logger.log(60, 'Mock data need update')
        mock_data_tools.update(data_path)
    elif mockdata_version < MOCK_DATA_V_1_0_0:
        logger.error('Can not update this mock data')

    # show current config contents
    print_lyrebird_info()
    config_str = json.dumps(application._cm.config, ensure_ascii=False, indent=4)
    logger.warning(f'Lyrebird start with config:\n{config_str}')

    # Main server
    application.server['event'] = EventServer()

    application.server['task'] = BackgroundTaskServer()
    application.server['proxy'] = LyrebirdProxyServer()
    application.server['mock'] = LyrebirdMockServer()
    application.server['db'] = LyrebirdDatabaseServer(path=args.database)
    application.server['plugin'] = PluginManager()
    application.server['checker'] = LyrebirdCheckerServer()

    application.start_server()

    # int statistics reporter
    application.reporter = reporter.Reporter()
    reporter.start()
    # activate notice center
    application.notice = NoticeCenter()

    # load debug plugin
    # TODO
    plugin_manager = application.server['plugin']
    if args.plugin:
        plugin_manager.plugin_path_list += args.plugin
    plugin_manager.reload()

    # load debug script
    if args.script:
        application.server['checker'].load_scripts(args.script)

    # auto open web browser
    if not args.no_browser:
        webbrowser.open(f'http://localhost:{application.config["mock.port"]}')

    # stop event handler
    def signal_handler(signum, frame):
        reporter.stop()
        application.stop_server()
        threading.Event().set()
        logger.warning('!!!Ctrl-C pressed. Lyrebird stop!!!')
        os._exit(1)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    threading.Event().wait()


def gen(args):
    parent_path = args.path
    project_name = input('Please input your project name:')
    if not project_name:
        print('Not set project name')
        return
    project_builder.make_plugin_project(project_name, parent_path+'/'+project_name)


def _get_ip():
    """
    Get local ip from socket connection

    :return: IP Addr string
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('bing.com', 80))
    return s.getsockname()[0]


def print_lyrebird_info():
    logo = [
        "",
        "",
        "     _                    _     _         _ ",
        "    | |                  | |   (_)       | |",
        "    | |    _   _ _ __ ___| |__  _ _ __ __| |",
        "    | |   | | | | '__/ _ \\ '_ \\| | '__/ _' |",
        "    | |___| |_| | | |  __/ |_) | | | | (_| |",
        "    \\_____/\\__, |_|  \\___|_.__/|_|_|  \\__,_|",
        "            __/ |                           ",
        "           |___/                            ",
        "",
        f"                   v{version.VERSION}",
        "",
        "",
        ""
    ]
    logo_str = '\n'.join(logo)
    # Custom log level 60  : NOTICE
    logger.log(60, logo_str)
