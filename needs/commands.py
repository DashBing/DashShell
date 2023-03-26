import os
from json import dumps as jen
from json import loads as jde
import ctypes
from .data import project_name,errormsg
import requests as rq

def listtostr(data):         # 列表连接文字
    s = ""
    for i in data:
        s = s + str(i)
    return(s)

def delstr(syn,text):        # 支持像列表一样通过索引删除特定项的函数
    a = list(text)
    del a[syn]
    return(listtostr(a))

def pathjoin(path1,path2):   # 连接目录(bug太多暂时废弃)
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

def init_pkgindex():        # 初始化软件home目录
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
            f.write(jen({"server":["https://raw.githubusercontent.com/DashBing/dspi/master/%s"],"pkgindex":{},"cmds":{}}))

def getmodulehandle(modulename):     # 取模块句柄(DLL命令在linux下会导致问题, 且本命令无实际意义, 仅作为一个依赖函数)
    user32 = ctypes.CDLL("Kernel32.dll")
    return(user32.GetModuleHandleA(ctypes.c_wchar(modulename)))

def loadicon(instance,ipiconname):   # 加载图标(同上)
    user32 = ctypes.CDLL("User32.dll")
    return(user32.LoadIconA(instance,ipiconname))

def about(title="Test",author="Test",hicon=loadicon(getmodulehandle(chr(0)),129)):     # 同上
    user32 = ctypes.CDLL("shell32.dll")
    user32.ShellAboutA(0,bytes(title,"gbk"),bytes(author,"gbk"),hicon)

def get_server_list():    # 获取源列表
    init_pkgindex()
    with open("./.%s/pkgindex.json"%project_name,"r") as f:
        l = f.read()
        l = jde(l)["server"]
    return(l)

def get_pkg_index(server):    # 获取包列表
    pl = rq.get(server%"index.json")
    pl = pl.content.decode("utf-8")
    pl = jde(pl)
    return(pl)

def get_server(syns):    # 通过索引获取列表中的源
    l = get_server_list()
    try:
        l = l[syns]
    except:
        l = l[0]
    return(l)

def ins_pkg(name,versionp,syns):    # 下载安装包(调用可能出错, 需与终端配合, 并记得返回调用前目录)
    server = get_server(syns)
    pl = get_pkg_index(server)
    try:
        fn = pl[name]
    except:
        print(errormsg%("错误，以下名称的软件包未找到：",name,"请检查是否输入正确！"))
    else:
        try:
            fn = fn[versionp]
        except:
            fn = fn[list(fn.keys())[0]]
        fr = rq.get(server%fn).content
        init_pkgindex()
        with open("./.%s/%s"%(project_name,fn),"wb") as f:
            f.write(fr)
        print("[%s] 安装成功。"%name)
