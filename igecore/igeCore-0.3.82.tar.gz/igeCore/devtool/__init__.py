"""
indi game engine offline develop tools

convert 3d assets
convert images to platform dipend format
make ige package
upload package to devserver

"""

import py_compile
import shutil
import glob
import os.path
import igeCore as core
from igeCore import apputil
from igeCore.devtool._igeTools import *
from igeCore import apputil
from igeCore.apputil import launch_server
import hashlib
import tokenize

def isHiddenFolder(path):
    if path.find('/.') != -1 or path.find('\\.') != -1 :
        return True
    return False

def findFiles(path, exts = ['.*']):
    list = []
    for root, dirs, files in os.walk(path):
        if isHiddenFolder(root): continue
        for fname in files:
            name, ext = os.path.splitext(fname)
            for e in exts:
                if e == '.*' or e == ext:
                    list.append(os.path.join(root, fname))
                    break
    return list

def findImageFiles(path):
    list = []
    for root, dirs, files in os.walk(path):
        if isHiddenFolder(root): continue
        for fname in files:
            name, ext = os.path.splitext(fname)
            if ext == '.png' or ext == '.dds' or ext == '.tga' or ext == '.psd':
                list.append(os.path.join(root, fname))
    return list

def find3DSceneFiles(path):
    dict = {}
    for root, dirs, files in os.walk(path):
        if root.find('\.') != -1: continue
        folder = os.path.basename(root)
        baseFile = folder + '.dae'

        folderRule = False
        for f in files:
            if f == baseFile:
                folderRule = True
                break

        if folderRule:
            daes = [os.path.join(root, baseFile)]
            for f2 in files:
                f2_name, f2_ext = os.path.splitext(f2)
                if f2_ext == '.dae' and f2_name != folder:
                    daes.append(os.path.join(root, f2))
            dict[folder] = daes
        else:
            for f2 in files:
                f2_name, f2_ext = os.path.splitext(f2)
                if f2_ext == '.dae':
                    dict[f2_name] = [os.path.join(root, f2)]
    return dict

def createDirectoryTree(filelist, root):
    imageDirectory = dict()
    for img in filelist:
        while True:
            img, file = os.path.split(img)
            if img not in imageDirectory:
                imageDirectory[img] = {file: 0};
            elif file not in imageDirectory[img]:
                imageDirectory[img][file] = 0
            if img == root: break
    return imageDirectory

def findFileFromDiorectoryTree(imageDirectory, file, dir):
    files = imageDirectory.get(dir)
    if files is None: return None
    if file in files:
        return os.path.join(dir, file)
    for d in files:
        _, ext = os.path.splitext(d)
        if ext is '':
            rv = findFileFromDiorectoryTree(imageDirectory, file, os.path.join(dir, d))
            if rv: return rv
    return None

def removeRoot(path, root):
    newpath = path.replace(root, '', 1)
    if len(newpath) >0:
        if newpath[0] == '/' or newpath[0] == '\\':
            newpath = newpath[1:]
    return newpath

def replaceExt(file, ext):
    name, extold = os.path.splitext(file)
    return name + ext

def readAndCalcHash(srcfile, dstfile, hashfile):
    hashcode = '00000000000000000000000000000000'
    newhash  = 'ffffffffffffffffffffffffffffffff'
    if os.path.exists(dstfile):
        try:
            with open(hashfile, 'r') as f:
                hashcode = f.read()
        except : None

    with open(srcfile, 'rb') as f:
        fileDataBinary = f.read()
        if len(fileDataBinary) is not 0:
            hash = hashlib.md5()
            hash.update(fileDataBinary)
            newhash = hash.hexdigest()
    return hashcode,newhash

def saveHash(hashfile, newhash):
    if newhash != 'ffffffffffffffffffffffffffffffff':
        apputil.makeDirectories(hashfile)
        with open(hashfile, 'w') as f:
            f.write(newhash)

def readFigureConf(path):
    mode = 0
    label = ''
    keyvalue = {}
    with open(path, 'rb') as f:
        for token in tokenize.tokenize(f.readline):
            if token.type is tokenize.ENDMARKER:
                break
            elif token.type is tokenize.NAME:
                if mode is 0:
                    label = token.string
                else:
                    keyvalue[label] = token.string
                    mode = 0
            elif token.type is tokenize.OP:
                mode = 1
            elif token.type is tokenize.NUMBER:
                if mode is 1:
                    try:
                        keyvalue[label] = int(token.string)
                    except ValueError:
                        keyvalue[label] = float(token.string)
                    mode = 0
    return keyvalue

def createFigureConfTree(path, unit=1.0):
    filelist = []
    for root, dirs, files in os.walk(path):
        if root.find('\.') != -1: continue
        for fname in files:
            if fname == 'figure.conf':
                filelist.append(os.path.join(root, fname))
    figureConfTree = dict()
    for filepath in filelist:
        conf = readFigureConf(filepath)
        dir, file = os.path.split(filepath)
        figureConfTree[dir] = conf

    for dir, val in figureConfTree.items():
        while True:
            dir, _ = os.path.split(dir)
            if len(dir) is 0:
                break
            parent = figureConfTree.get(dir)
            if parent is not None:
                for parentkey, parentval in parent.items():
                    if val.get(parentkey) is None:
                        val[parentkey] = parentval

    if len(figureConfTree) == 0:
        figureConfTree['.'] = {}

    for conf in figureConfTree.values():
        if conf.get('BASE_SCALE') is None:
           conf['BASE_SCALE'] = unit

    return figureConfTree

def findFigureConf(dir: str, tree: dict):
    while True:
        dir, _ = os.path.split(dir)
        if len(dir) is 0:
            break
        conf = tree.get(dir)
        if conf is not None:
            return conf
    return dict()

def load3DScene(tmpfig, files, conf):
    loadCollada(files[0], tmpfig, conf)
    for i in range(1, len(files)):
        loadColladaAnimation(files[i], tmpfig, conf)

def replaceTexturePath(tmpfig, imageDirectory, startPath, endPath, allTextures):
    texs = tmpfig.getTextureSource()
    for tex in texs:
        filename = os.path.basename(tex['path'])
        current = startPath
        inputimage = None
        while True:
            inputimage = findFileFromDiorectoryTree(imageDirectory, filename, current)
            if inputimage is not None: break
            if current == endPath: break
            current, _ = os.path.split(current)
        if inputimage is None:
            print('file not found ' + tex['path'])
        else:
            allTextures[inputimage] = tex;
            inputimage = inputimage.replace('\\', '/')
            inputimage = removeRoot(inputimage, endPath);
            inputimage, ext = os.path.splitext(inputimage)
            newTex = {'path': inputimage, 'normal': tex['normal'], 'wrap': tex['wrap']}
            tmpfig.replaceTextureSource(tex, newTex)

def getHashPath(root, source, platform):
    abspath = os.path.abspath(source)
    if abspath[0]=='/' or abspath[0]=='\\':
       abspath = abspath[1:]
    elif abspath[2]=='\\':
        abspath = abspath[3:]
    return os.path.join(os.path.join(root, apputil.platformName(platform)), abspath)

def convertImages(allTextures, sourceDir, destDir, platform):
    print('----------------------')
    print('Convert image files')
    print('----------------------')
    for key, val in allTextures.items():
        outfile = os.path.normpath(key.replace(sourceDir, destDir, 1))
        outfile = replaceExt(outfile, '.pyxi')
        hashfile = getHashPath('.tmp/hash', key, platform)
        hashcode, newhash = readAndCalcHash(key, outfile, hashfile)
        if hashcode != newhash:
            print("convert {} for {}".format(key,apputil.platformName(platform)))
            apputil.makeDirectories(outfile)
            convertTextureToPlatform(key, outfile, platform, val['normal'], val['wrap'])
            saveHash(hashfile, newhash)
        else:
            print("skip convert {} because no change".format(key))

def copyFiles(src, dst, exts=['.*']):
    for root, dirs, files in os.walk(src):
        if isHiddenFolder(root): continue
        for fname in files:
            name, ext = os.path.splitext(fname)
            for e in exts:
                if e == '.*' or ext == e:
                    srcPath = os.path.join(root, fname)
                    dstPath = os.path.join(dst, removeRoot(srcPath, src))
                    apputil.makeDirectories(dstPath)
                    shutil.copy2(srcPath, dstPath)
                    print("copy {}".format(dstPath))
                    break

def compilePrograms(src, dst):
    list = findFiles(src, ['.py'])
    for infile in list:
        outfile = os.path.normpath(infile.replace(src, dst, 1))
        apputil.makeDirectories(outfile)
        if os.path.basename(infile) == 'root.py':
            shutil.copy(infile, outfile)
        else:
            outfile = replaceExt(outfile, '.pyc')
            apputil.makeDirectories(outfile)
            print('compile : '+infile)
            py_compile.compile(infile, outfile)

def hashCheck(files, outfile, platform):
    changed = False
    for file in files:
        hashfile = getHashPath('.tmp/hash', file, platform)
        hashcode, newhash = readAndCalcHash(file, outfile, hashfile)
        if hashcode != newhash:
            changed = True
            saveHash(hashfile, newhash)
    return changed

def buildAppPackage(src, dest):
    apputil.makeDirectories(dest)
    list =glob.glob(os.path.join(src,'*' ))
    for dir in list:
        if os.path.isdir(dir):
            outpath = os.path.join(dest,os.path.basename(dir))

            list = findFiles(dir)
            if hashCheck(list, outpath+'.pyxd', 0):
                print("build asset database {}.pyxd".format(outpath))
                compressFolder(dir, outpath)
            else:
                print("skip asset database {}.pyxd".format(outpath))
        else:
            print("copy {}".format(dir))
            shutil.copy2(dir, dest)

def convertAssets(sourceDir, destDir, platform, unit=1.0):
    """
    Convert model and image data to ige format
    model(.dae) -> .pyxf
    image(.png .dds .tga .psd ) -> .pyxi

    If model data with the same name as the folder name is found,
    it is regarded as base model data, and other model data in the
    same folder are regarded as motion files, and all are packed
    into one file
    If there is no model data with the same name as the folder name,
    Each model data as base model data and convert separately

    :param sourceDir: source root folder
    :param destDir: destination root folder
    :param platform: target platform (core.TARGET_PLATFORM_XX)
    :param unit: scale unit size of 3d model
    :return: None
    """

    imageList = findImageFiles(sourceDir)
    sceneList = find3DSceneFiles(sourceDir)
    imageDirectoryTree = createDirectoryTree(imageList, sourceDir)
    confTree = createFigureConfTree(sourceDir, unit)
    allTextures = dict()
    tmpfig = core.editableFigure("tmpfigure")

    print('----------------------')
    print('Convert 3d scene files')
    print('----------------------')

    for files in sceneList.values():

        tmpfig.clear()
        conf = findFigureConf(files[0], confTree)
        load3DScene(tmpfig, files, conf)

        daepath, _ = os.path.split(files[0])
        replaceTexturePath(tmpfig, imageDirectoryTree, daepath, sourceDir, allTextures)

        outfile = os.path.normpath(files[0].replace(sourceDir, destDir, 1))
        outfile = replaceExt(outfile, '.pyxf')

        if hashCheck(files, outfile, platform):
            print("convert {}".format(files[0]))
            apputil.makeDirectories(outfile)
            tmpfig.mergeMesh()
            tmpfig.saveFigure(outfile)
        else:
            print("skip {}".format(files[0]))

    print('----------------------')
    print('Convert image files')
    print('----------------------')
    for img in imageList:
        if img not in allTextures:
            allTextures[img] = {'path': removeRoot(img,sourceDir), 'normal': False, 'wrap': False}

    convertImages(allTextures, sourceDir, destDir, platform)

    return allTextures




def deploy(projectFolder, userID, appName, appVersion, unit = 1.0, assetSource=None, assetDestination=None):
    if assetSource == None: assetSource = projectFolder
    if assetDestination == None: assetDestination = projectFolder
    allTextures = convertAssets(assetSource, assetDestination, core.TARGET_PLATFORM_PC, unit)

    deployTmp = '.tmp/deploy/'+appName+'/'+appVersion+'/'

    print('----------------------')
    print('Create non pack app image')
    print('----------------------')
    copyFiles(projectFolder, deployTmp+'unpackimage/pc', ['.pyxf', '.json', '.pyxa', '.pyxb', '.pickle', '.zip', '.txt', '.db', '.ttf'])
    compilePrograms(projectFolder, deployTmp+'unpackimage/pc')
    copyFiles(deployTmp+'unpackimage/pc', deployTmp+'unpackimage/ios')
    copyFiles(deployTmp+'unpackimage/pc', deployTmp+'unpackimage/android')
    copyFiles(projectFolder, deployTmp+'unpackimage/pc', ['.pyxi'])
    convertImages(allTextures, assetSource, deployTmp+removeRoot(projectFolder, assetDestination), core.TARGET_PLATFORM_IOS)
    convertImages(allTextures, assetSource, deployTmp+removeRoot(projectFolder, assetDestination), core.TARGET_PLATFORM_ANDROID)

    print('----------------------')
    print('Create packed app image')
    print('----------------------')
    buildAppPackage(deployTmp+'unpackimage/pc', deployTmp+'packimage/pc')
    buildAppPackage(deployTmp+'unpackimage/ios', deployTmp+'packimage/ios')
    buildAppPackage(deployTmp+'unpackimage/android', deployTmp+'packimage/android')

    print('----------------------')
    print('Upload app image to the server')
    print('----------------------')
    launch_server.makeProjectDir(userID, appName, appVersion, "pc")
    launch_server.upload_files(deployTmp+'packimage/pc', '/'+userID+'/'+appName+'/'+appVersion+'/pc')
    launch_server.makeProjectDir(userID, appName, appVersion, "ios")
    launch_server.upload_files(deployTmp+'packimage/ios',  '/'+userID+'/'+appName+'/'+appVersion+'/ios')
    launch_server.makeProjectDir(userID, appName, appVersion, "android")
    launch_server.upload_files(deployTmp+'packimage/android',  '/'+userID+'/'+appName+'/'+appVersion+'/android')
