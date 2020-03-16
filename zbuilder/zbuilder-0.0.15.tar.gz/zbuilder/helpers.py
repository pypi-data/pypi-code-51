import sys
import click
import time
import socket
import delegator
import ruamel.yaml
import zbuilder.vm
import zbuilder.cfg

from retrying import retry
from ansible.cli import CLI
from ansible.errors import AnsibleError
from ansible.template import Templar
from ansible.cli.playbook import PlaybookCLI


def getVars():
    parser = CLI.base_parser(vault_opts=True, inventory_opts=True)
    options, args = parser.parse_args(["-i", "hosts"])
    loader, inventory, vm = CLI._play_prereqs(options)
    hosts = inventory.get_hosts(pattern='localhost')
    tVars = vm.get_vars(host=hosts[0])
    retValue = {}
    for v in tVars:
        if v == 'VM_OPTIONS':
            next
        if v.startswith('ZBUILDER_'):
            retValue[v] = tVars[v]
    return retValue


def getHostsWithVars(subset):
    parser = CLI.base_parser(vault_opts=True, inventory_opts=True)
    options, args = parser.parse_args(["-i", "hosts", "-l", subset.limit])
    loader, inventory, vm = CLI._play_prereqs(options)

    hostVars = {}
    for host in inventory.get_hosts():
        hvars = vm.get_vars(host=host, include_hostvars=True)
        templar = Templar(loader=loader, variables=hvars)
        hvars = templar.template(hvars)

        if 'ZBUILDER_PROVIDER' in hvars:
            hvars['ZBUILDER_PROVIDER']['VM_OPTIONS']['enabled'] = False
            hostVars[host.name] = hvars['ZBUILDER_PROVIDER']
            if 'ansible_host' in hvars:
                hostVars[host.name]['ansible_host'] = hvars['ansible_host']
            if 'ZBUILDER_PUBKEY' in hvars:
                hostVars[host.name]['ZBUILDER_PUBKEY'] = hvars['ZBUILDER_PUBKEY']
            if 'ZBUILDER_SYSUSER' in hvars:
                hostVars[host.name]['ZBUILDER_SYSUSER'] = hvars['ZBUILDER_SYSUSER']

    inventory.subset(options.subset)
    for host in inventory.get_hosts():
        if host.name in hostVars:
            hostVars[host.name]['VM_OPTIONS']['enabled'] = True

    return hostVars


def getHosts(state):
    state.vars = getVars()
    cfg = zbuilder.cfg.load()
    hosts = getHostsWithVars(state)

    vmProviders = {}
    if cfg is None:
        click.Abort("Config file seems to be empty")
    if 'providers' not in cfg:
        click.Abort("There is no 'providers' sections on config file")

    for h, hvars in hosts.items():
        if 'CLOUD' in hvars:
            curVMProvider = hvars['CLOUD']
        else:
            next

        if curVMProvider not in vmProviders:
            provider_cfg = cfg['providers'][curVMProvider]
            provider_cfg['state'] = state
            vmProviders[curVMProvider] = {
                'cloud': zbuilder.vm.vmProvider(provider_cfg['type'], provider_cfg),
                'hosts': {}
            }

        hvars['VM_OPTIONS']['aliases'] = ''
        if 'ansible_host' in hvars:
            hvars['VM_OPTIONS']['ansible_host'] = hvars['ansible_host']
        if 'ZBUILDER_PUBKEY' in hvars:
            hvars['VM_OPTIONS']['ZBUILDER_PUBKEY'] = hvars['ZBUILDER_PUBKEY']
        if 'ZBUILDER_SYSUSER' in hvars:
            hvars['VM_OPTIONS']['ZBUILDER_SYSUSER'] = hvars['ZBUILDER_SYSUSER']

        vmProviders[curVMProvider]['hosts'][h] = hvars['VM_OPTIONS']

    return vmProviders


def runPlaybook(state, pbook):
    try:
        playbookCLI = PlaybookCLI(["ansible-playbook", "-l", state.limit,  pbook])
        playbookCLI.parse()
        playbookCLI.run()
    except AnsibleError as e:
        click.echo(e)


def load_yaml(fname):
    """Safely load a yaml file"""
    value = None
    try:
        yaml = ruamel.yaml.YAML()
        with open(fname, 'r') as f:
            value = yaml.load(f)
    except ruamel.yaml.YAMLError as e:
        if hasattr(e, 'problem_mark'):
            mark = e.problem_mark
            raise click.ClickException(
                "Yaml error (%s) at position: [line:%s column:%s]" %
                (fname, mark.line + 1, mark.column + 1)
            )
    except Exception as e:
        raise click.ClickException(e)

    return value


def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d' % (mins, secs)


def dump_yaml(cfg, where=None):
    yaml = ruamel.yaml.YAML()
    if where:
        yaml.dump(cfg, where)
    else:
        yaml.dump(cfg, sys.stdout)


@retry(stop_max_delay=10000)
def getIP(hostname):
    return socket.gethostbyname(hostname)


def waitSSH(ip):
    TIMEOUT = 300
    start_time = time.perf_counter()
    while True:
        try:
            with socket.create_connection((ip, 22), timeout=TIMEOUT):
                break
        except OSError:
            time.sleep(0.01)
            if time.perf_counter() - start_time >= TIMEOUT:
                return None
    return True


def fixKeys(state):
    vmProviders = getHosts(state)
    for _, vmProvider in vmProviders.items():
        for h, v in vmProvider['hosts'].items():
            if v['enabled']:
                ip = None
                if 'ansible_host' in v:
                    ip = v['ansible_host']
                else:
                    try:
                        ip = getIP(h)
                    except Exception:
                        click.echo(click.style("  - Host: {} can't be resolved".format(h), fg='red'))
                        continue

                click.echo("  - Host: {}".format(h))
                runCmd("ssh-keygen -R {}".format(h), verbose=state.verbose)
                if ip is not None:
                    runCmd("ssh-keygen -R {}".format(ip), verbose=state.verbose)
                    waitSSH(ip)
                    runCmd(
                        "ssh -o StrictHostKeyChecking=no -o PasswordAuthentication=no {} exit".format(h),
                        verbose=state.verbose, ignoreError=True
                    )
                    runCmd(
                        "ssh -o StrictHostKeyChecking=no -o PasswordAuthentication=no {} exit".format(ip),
                        verbose=state.verbose, ignoreError=True
                    )


def runCmd(cmd, verbose=False, dry=False, ignoreError=False):
    if verbose:
        click.echo("    CMD: [{}]".format(cmd))
    if not dry:
        status = delegator.run(cmd)
        if verbose:
            click.echo(click.style(status.out, fg='green'))
        if status.return_code != 0 and not ignoreError:
            click.echo(click.style(status.err, fg='red'))

    return status.return_code
