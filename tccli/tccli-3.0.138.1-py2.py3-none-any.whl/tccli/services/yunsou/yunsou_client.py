# -*- coding: utf-8 -*-
import os
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli.nice_command import NiceCommand
import tccli.error_msg as ErrorMsg
import tccli.help_template as HelpTemplate
from tccli import __version__
from tccli.utils import Utils
from tccli.configure import Configure
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.yunsou.v20191115 import yunsou_client as yunsou_client_v20191115
from tencentcloud.yunsou.v20191115 import models as models_v20191115
from tencentcloud.yunsou.v20180504 import yunsou_client as yunsou_client_v20180504
from tencentcloud.yunsou.v20180504 import models as models_v20180504
from tccli.services.yunsou import v20191115
from tccli.services.yunsou.v20191115 import help as v20191115_help
from tccli.services.yunsou import v20180504
from tccli.services.yunsou.v20180504 import help as v20180504_help


def doDataManipulation(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DataManipulation", g_param[OptionsDefine.Version])
        return

    param = {
        "OpType": argv.get("--OpType"),
        "Encoding": argv.get("--Encoding"),
        "Contents": argv.get("--Contents"),
        "ResourceId": Utils.try_to_json(argv, "--ResourceId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.YunsouClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DataManipulationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DataManipulation(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDataSearch(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DataSearch", g_param[OptionsDefine.Version])
        return

    param = {
        "ResourceId": Utils.try_to_json(argv, "--ResourceId"),
        "SearchQuery": argv.get("--SearchQuery"),
        "PageId": Utils.try_to_json(argv, "--PageId"),
        "NumPerPage": Utils.try_to_json(argv, "--NumPerPage"),
        "SearchId": argv.get("--SearchId"),
        "QueryEncode": Utils.try_to_json(argv, "--QueryEncode"),
        "RankType": Utils.try_to_json(argv, "--RankType"),
        "NumFilter": argv.get("--NumFilter"),
        "ClFilter": argv.get("--ClFilter"),
        "Extra": argv.get("--Extra"),
        "SourceId": Utils.try_to_json(argv, "--SourceId"),
        "SecondSearch": Utils.try_to_json(argv, "--SecondSearch"),
        "MaxDocReturn": Utils.try_to_json(argv, "--MaxDocReturn"),
        "IsSmartbox": Utils.try_to_json(argv, "--IsSmartbox"),
        "EnableAbsHighlight": Utils.try_to_json(argv, "--EnableAbsHighlight"),
        "QcBid": Utils.try_to_json(argv, "--QcBid"),
        "GroupBy": argv.get("--GroupBy"),
        "Distinct": argv.get("--Distinct"),
        "L4RankExpression": argv.get("--L4RankExpression"),
        "MatchValue": argv.get("--MatchValue"),
        "Longitude": Utils.try_to_json(argv, "--Longitude"),
        "Latitude": Utils.try_to_json(argv, "--Latitude"),
        "MultiFilter": Utils.try_to_json(argv, "--MultiFilter"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.YunsouClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DataSearchRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DataSearch(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20191115": yunsou_client_v20191115,
    "v20180504": yunsou_client_v20180504,

}

MODELS_MAP = {
    "v20191115": models_v20191115,
    "v20180504": models_v20180504,

}

ACTION_MAP = {
    "DataManipulation": doDataManipulation,
    "DataSearch": doDataSearch,

}

AVAILABLE_VERSION_LIST = [
    v20191115.version,
    v20180504.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20191115.version.replace('-', ''): {"help": v20191115_help.INFO,"desc": v20191115_help.DESC},
     'v' + v20180504.version.replace('-', ''): {"help": v20180504_help.INFO,"desc": v20180504_help.DESC},

}


def yunsou_action(argv, arglist):
    if "help" in argv:
        versions = sorted(AVAILABLE_VERSIONS.keys())
        opt_v = "--" + OptionsDefine.Version
        version = versions[-1]
        if opt_v in argv:
            version = 'v' + argv[opt_v].replace('-', '')
        if version not in versions:
            print("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
            return
        action_str = ""
        docs = AVAILABLE_VERSIONS[version]["help"]
        desc = AVAILABLE_VERSIONS[version]["desc"]
        for action, info in docs.items():
            action_str += "        %s\n" % action
            action_str += Utils.split_str("        ", info["desc"], 120)
        helpstr = HelpTemplate.SERVICE % {"name": "yunsou", "desc": desc, "actions": action_str}
        print(helpstr)
    else:
        print(ErrorMsg.FEW_ARG)


def version_merge():
    help_merge = {}
    for v in AVAILABLE_VERSIONS:
        for action in AVAILABLE_VERSIONS[v]["help"]:
            if action not in help_merge:
                help_merge[action] = {}
            help_merge[action]["cb"] = ACTION_MAP[action]
            help_merge[action]["params"] = []
            for param in AVAILABLE_VERSIONS[v]["help"][action]["params"]:
                if param["name"] not in help_merge[action]["params"]:
                    help_merge[action]["params"].append(param["name"])
    return help_merge


def register_arg(command):
    cmd = NiceCommand("yunsou", yunsou_action)
    command.reg_cmd(cmd)
    cmd.reg_opt("help", "bool")
    cmd.reg_opt(OptionsDefine.Version, "string")
    help_merge = version_merge()

    for actionName, action in help_merge.items():
        c = NiceCommand(actionName, action["cb"])
        cmd.reg_cmd(c)
        c.reg_opt("help", "bool")
        for param in action["params"]:
            c.reg_opt("--" + param, "string")

        for opt in OptionsDefine.ACTION_GLOBAL_OPT:
            stropt = "--" + opt
            c.reg_opt(stropt, "string")


def parse_global_arg(argv):
    params = {}
    for opt in OptionsDefine.ACTION_GLOBAL_OPT:
        stropt = "--" + opt
        if stropt in argv:
            params[opt] = argv[stropt]
        else:
            params[opt] = None
    if params[OptionsDefine.Version]:
        params[OptionsDefine.Version] = "v" + params[OptionsDefine.Version].replace('-', '')

    config_handle = Configure()
    profile = config_handle.profile
    if ("--" + OptionsDefine.Profile) in argv:
        profile = argv[("--" + OptionsDefine.Profile)]

    is_conexist, conf_path = config_handle._profile_existed(profile + "." + config_handle.configure)
    is_creexist, cred_path = config_handle._profile_existed(profile + "." + config_handle.credential)
    config = {}
    cred = {}
    if is_conexist:
        config = config_handle._load_json_msg(conf_path)
    if is_creexist:
        cred = config_handle._load_json_msg(cred_path)

    for param in params.keys():
        if param == OptionsDefine.Version:
            continue
        if params[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId]:
                if param in cred:
                    params[param] = cred[param]
                else:
                    raise Exception("%s is invalid" % param)
            else:
                if param in config:
                    params[param] = config[param]
                elif param == OptionsDefine.Region:
                    raise Exception("%s is invalid" % OptionsDefine.Region)
    try:
        if params[OptionsDefine.Version] is None:
            version = config["yunsou"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["yunsou"][OptionsDefine.Endpoint]
    except Exception as err:
        raise Exception("config file:%s error, %s" % (conf_path, str(err)))
    versions = sorted(AVAILABLE_VERSIONS.keys())
    if params[OptionsDefine.Version] not in versions:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
    return params


def show_help(action, version):
    docs = AVAILABLE_VERSIONS[version]["help"][action]
    desc = AVAILABLE_VERSIONS[version]["desc"]
    docstr = ""
    for param in docs["params"]:
        docstr += "        %s\n" % ("--" + param["name"])
        docstr += Utils.split_str("        ", param["desc"], 120)

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "yunsou", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["yunsou"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
