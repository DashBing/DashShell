import os
from json import dumps as jen
from json import dumps as jde
import ctypes
from .data import project_name

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
        homepath = os.getenv("%sHome"%project_name)
        if homepath == None:
            homepath = os.getcwd()
            os.putenv("%sHome"%project_name,homepath)
    except:
        homepath = os.getcwd()
        os.putenv("%sHome"%project_name,homepath)
    try:
        try:
            os.mkdir("%s/.%s"%(homepath,project_name))
        except:
            os.mkdir("%s\\.%s"%(homepath,project_name))
        #os.mkdir(pathjoin(homepath,".DashShell"))
    except:
        pass
    try:
        os.chdir(homepath)
    except:
        os.chdir(homepath)
    try:
        with open("./.%s/pkgindex.json"%project_name,"r") as f:
            pass
    except:
        with open("./.%s/pkgindex.json"%project_name,"w") as f:
            f.write(jen({}))

def getmodulehandle(modulename):
    user32 = ctypes.CDLL("Kernel32.dll")
    return(user32.GetModuleHandleA(ctypes.c_wchar(modulename)))

def loadicon(instance,ipiconname):
    user32 = ctypes.CDLL("User32.dll")
    return(user32.LoadIconA(instance,ipiconname))

def about(title="Test",author="Test",hicon=loadicon(getmodulehandle(chr(0)),129)):
    user32 = ctypes.CDLL("shell32.dll")
    user32.ShellAboutA(0,bytes(title,"gbk"),bytes(author,"gbk"),hicon)
