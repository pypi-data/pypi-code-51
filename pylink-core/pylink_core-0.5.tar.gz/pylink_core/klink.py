# -*- coding:utf-8 -*-
import sys, os
import json
import argparse
import logging
import time
import threading
import struct
import base64
import shutil
from .ExecThread import *

from .Uf2Manager import *
from .SerialCom import serialList, serialCom
from .uflash import getDisk
from .ImageManager import saveToBmp

from flask import Flask,send_from_directory,abort,make_response
from flask_sockets import Sockets

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

extensions = {
    'meowbit': {
        "id": "meowbit",
        "fullpath": os.getcwd(),
        "name": "Meowbit",
        "name_zh": "喵比特",
        "version": "1.0.0",
        "type": "micropy",
        "fwtype": "uf2",
        "replmode": True,
        "execmode": True,
        "firmware": "firmware.uf2",
        "thumbdisk": "PYBFLASH"
    }
}
userPath = None
pioPath = None
server = None
uihandler = None
cloudVar = {}
cloudClients = {}

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

try:
    import sentry_sdk
    sentry_sdk.init("http://a845fedc49424ec7b1933bf645dd1ae9@bug.kittenbot.cn:99/3")
except:
    logger.warn("Sentry not installed, try: pip install --upgrade sentry-sdk==0.14.2")
    pass


class LoggingSlot(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        msg = self.format(record)
        uihandler("log", msg)

def enumExtensionDir(args):
    global userPath
    userPath = args.user
    logger.info("User Path: %s" %userPath)


app = Flask(__name__)
sockets = Sockets(app)

def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)

@sockets.route('/cloud')
def cloud_socket(ws):
    logger.info("Cloud Socket %s" %ws)
    cloudClients[ws.origin] = ws
    while not ws.closed:
        try:
            message = ws.receive()
            if not message:
                continue
            obj = json.loads(message)
            logger.info("Cloud >> %s" %obj)
            if obj['method'] == 'handshake':
                for var in cloudVar:
                    ret = {
                        'method': 'set',
                        'name': var,
                        'value': cloudVar[var]
                    }
                    ws.send(json.dumps(ret))
            elif obj['method'] == 'create':
                cloudVar[obj['name']] = obj['value']
            elif obj['method'] == 'set':
                var = obj['name']
                cloudVar[var] = obj['value']
                for orig in cloudClients:
                    if orig != ws.origin:
                        ret = {
                            'method': 'set',
                            'name': var,
                            'value': cloudVar[var]
                        }
                        ws.send(json.dumps(ret))

            
        except Exception as err:
            logger.error("WS err %s" %err)
            continue
    del cloudVar[ws.origin]
    logger.info("Cloud Socket closed")

@sockets.route('/')
def echo_socket(ws):
    logger.info("New socket %s" %ws)
    ext = None
    comm = None
    commType = None
    commList = []
    uploadTh = None
    def sendResp(pid, result, error=None):
        res = {
            "jsonrpc":"2.0",
            "id": pid,
            "result": result
        }
        if error:
            res['error'] = error
        ws.send(json.dumps(res))
    def sendReq(method, params={}):
        req = {
            "jsonrpc":"2.0",
            "method":method,
            "params": params
        }
        ws.send(json.dumps(req))
    def commRx(msg, dt):
        if msg == None and dt == -1:
            sendReq('connclose')
        else:
            b64 = str(base64.b64encode(msg), 'utf8')
            sendReq("data", {"data": b64})
    while not ws.closed:
        message = ws.receive()
        if not message:
            continue
        try:
            obj = json.loads(message)
            if 'id' in obj:
                pid = obj['id']
            if 'params' in obj:
                params = obj['params']
            method = obj['method']
            # logger.info(">> %s" %obj)
            if method == 'sync':
                extId = params['extensionId']
                ext = extensions[extId]
                sendResp(pid, ext)
                uihandler("showmsg", "connected", "extension %s loaded" %extId)
            elif method == 'listdevice':
                serPorts = serialList()
                commList = serPorts
                sendResp(pid, commList)
            elif method == 'connect':
                
                peripheralId = params['peripheralId']
                port = None
                for p in commList:
                    if p['peripheralId'] == peripheralId:
                        port = p
                        break
                
                if p['type'] == 'serial':
                    comm = serialCom(commRx)
                    comm.connect(p['peripheralId'], baud=115200)
                    commType = 'serial'
                sendResp(pid, p)
            elif method == 'auto-connect':
                # auto connect only valid in serial ports
                config = params['config']
                serPorts = serialList()
                for s in serPorts:
                    if s['pid'] == config['pid'] and s['vid'] == config['vid']:
                        logger.info("auto connect to %s " %(s))
                        comm = serialCom(commRx)
                        comm.connect(s['peripheralId'], baud=115200)
                        commType = 'serial'
                        sendResp(pid, s)
                        break
            elif method == 'list-file':
                dest = getDisk(ext['thumbdisk'])
                if dest:
                    fileFilter = None
                    if 'filter' in params:
                        fileFilter = params['filter']
                    files = os.listdir(dest)
                    allFiles = []
                    for f in files:
                        fileExtension = os.path.splitext(f)[1]
                        if fileFilter:
                            if fileExtension in fileFilter:
                                allFiles.append(f)
                        else:
                            allFiles.append(f)
                    sendResp(pid, {'files': allFiles})
                else:
                    sendResp(pid, {'err':'no_disk'})
            elif method == 'delete-file':
                dest = getDisk(ext['thumbdisk'])
                ret = -1
                if dest:
                    fileName = params['fileName']
                    filePath = os.path.join(dest, fileName)
                    if os.path.exists(filePath):
                        os.remove(filePath)
                        ret = 0
                sendReq("extension-method", {"extensionId": ext['id'], "func": "onDelDone", "msg": ret})
            elif method == 'upload-file':
                dest = getDisk(ext['thumbdisk'])
                if not dest:
                    sendReq("extension-method", {"extensionId": ext['id'], "func": "onError", "msg": 'no_device'})
                    continue
                fileName = params['fileName']
                destPath = os.path.join(dest, fileName)
                with open(destPath, 'wb') as output:
                    logger.info("copy %s to %s" %(fileName, destPath))
                    content = base64.b64decode(params['content'])
                    output.write(content)
                    sendReq("extension-method", {"extensionId": ext['id'], "func": "onCopyDone", "msg": destPath})
            elif method == 'upload-image':
                dest = getDisk(ext['thumbdisk'])
                if not dest:
                    sendReq("extension-method", {"extensionId": ext['id'], "func": "onError", "msg": 'no_device'})
                    continue
                fileName = params['fileName']
                destPath = os.path.join(dest, fileName)
                width = None
                if 'width' in params:
                    width = int(params['width'])
                destPath = os.path.splitext(destPath)[0]+'.bmp'
                saveToBmp(params['content'], destPath, width)
                sendReq("extension-method", {"extensionId": ext['id'], "func": "onCopyDone", "msg": destPath})
            elif method == 'upload-firmware':
                if ext["fwtype"] == "uf2":
                    uploadUf2(ext, params, sendReq, userPath)
            elif method == 'upload-stop':
                # if uploadTh:
                #     uploadTh.killTh()
                sendReq("upload-status")
            elif method == 'write':
                msg = params['data']
                msg = base64.b64decode(msg)
                if comm:
                    comm.write(msg)
            elif method == 'disconnect':
                if comm:
                    comm.close()
            else:
                ws.send('{"jsonrpc":"2.0"}')
        except Exception as err:
            logger.error("WS err %s" %err)
            if sentry_sdk:
                sentry_sdk.capture_exception(err)
            continue
    logger.info("## WS connection closed")
    if comm:
        comm.close()

@app.route('/extension/list')
def extensionList():
    extList = []
    for key in extensions:
        extList.append(extensions[key])
    return json.dumps(extList)
    # rst = make_response(json.dumps(extList))
    # rst.headers['Access-Control-Allow-Origin'] = '*'
    # return rst, 201

def testRequest(parama, paramb):
    logger.info("test req %s %s" %(parama, paramb))
    return "test req %s %s" %(parama, paramb)

def klinkServe(args, logCallback=None):
    global server, uihandler
    if logCallback:
        uihandler = logCallback
        loghd = LoggingSlot()
        logging.getLogger().addHandler(loghd)
    # prepare for extension
    enumExtensionDir(args)
    # logger.info(json.dumps(extensions, sort_keys=True, indent=4))

    # app.add_url_rule('/test/<parama>/<paramb>', view_func=testRequest)

    server = pywsgi.WSGIServer(('0.0.0.0', args.port), app, handler_class=WebSocketHandler)
    logger.info("web server start ... ")
    server.serve_forever()


def shutdown():
    logger.info("web server shutdown")
    server.stop()
    server.close()
    
