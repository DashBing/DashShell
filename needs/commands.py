import os
from json import dumps as jen
from json import dumps as jde
import ctypes

def listtostr(data):         # 列表连接文字
    s = ""
    for i in data:
        s = s + str(i)
    return(s)

def delstr(syn,text):        # 支持像列表一样通过索引删除特定项的函数
    a = list(text)
    del a[syn]
    return(listtostr(a))

def pathjoin(path1,path2):
    if "\\" in path1:
        return(os.path.join(path1,path2))
    else:
        if path1[-1] == "/" or path2[0] == "/":
            if path1[-1] == "/" and path2[0] == "/":
                return(path1 + delstr(0,path2))
            else:
                return(path1 + path2)
        else:
            return(path1 + "/" + path2)

def init_pkgindex():
    try:
        homepath = os.getenv("DashShellHome")
    except:
        homepath = os.getcwd()
        os.putenv("DashShellHome",homepath)
    try:
        try:
            os.mkdir("%s/.DashShell"%homepath)
        except:
            os.mkdir("%s\\.DashShell"%homepath)
        #os.mkdir(pathjoin(homepath,".DashShell"))
    except:
        pass
    try:
        os.chdir("%s/.DashShell"%homepath)
    except:
        os.chdir("%s\\.DashShell"%homepath)
    try:
        with open("./DashShell/pkgindex.json","r") as f:
            pass
    except:
        with open("./DashShell/pkgindex.json","w") as f:
            f.write(jen({}))

def getmodulehandle(modulename):
    user32 = ctypes.CDLL("Kernel32.dll")
    return(user32.GetModuleHandleA(ctypes.c_wchar(modulename)))

def loadicon(instance,ipiconname):
    user32 = ctypes.CDLL("User32.dll")
    return(user32.LoadIconA(instance,ipiconname))

def about(title="Test",author="Test",hicon=loadicon(getmodulehandle(chr(0)),129)):
    user32 = ctypes.CDLL("shell32.dll")
    user32.ShellAboutA(0,bytes(title,"utf-8"),bytes(author,"utf-8"),hicon)
