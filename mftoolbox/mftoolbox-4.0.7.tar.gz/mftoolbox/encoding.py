import sys as _sys

def encoding():
    # define no encoding baseado no sistema operacional
    # arquivo em Windows (win32) tem que ser salvo em Unicode
    # se for Mac (darwin) tem que ser salvo como UTF-8
    str_platform = _sys.platform
    if str_platform == 'win32':
        return 'utf_16'
    elif str_platform == 'darwin':
        return 'utf_8'