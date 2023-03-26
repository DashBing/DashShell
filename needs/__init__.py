import os
import sys
from json import dumps as jen
from json import dumps as jde
from .data import errormsg,helps,preprint,version,copyright,project_name
from .commands import init_pkgindex,about,ins_pkg,get_server_list,get_pkg_index
import threading
import ctypes
import requests as rq

def main():
    print(preprint)
    tmpcwd = os.getcwd()
    init_pkgindex()
    os.chdir(tmpcwd)
    del tmpcwd
    pkg_theads = {}
    theads = []
    while True:
        inp = input("%s>"%os.getcwd())
        if inp != "":
            inpl = inp.split(" ")
            match inpl[0]:
                case "cd":
                    tmp = inp[3:len(inp)]
                    try:
                        os.chdir(tmp)
                    except:
                        try:
                            del theads[-1]
                        except:
                            pass
                        print(errormsg%("未找到相关目录：",tmp,"请检查目录名称是否正确。"))
                case "进入":
                    tmp = inp[3:len(inp)]
                    try:
                        os.chdir(tmp)
                    except:
                        try:
                            del theads[-1]
                        except:
                            pass
                        print(errormsg%("未找到相关目录：",tmp,"请检查目录名称是否正确。"))
                case "包":
                    match inpl[1]:
                        case "安装":
                            tmp = inp[5:len(inp)]
                            sl = get_server_list()
                            for i in range(len(sl)):
                                print("[%s] %s"%(i,sl[i]))
                            l = input("请选择其中一个源进行下载（默认为第一个）:\n?.>")
                            try:
                                l = int(l)
                            except:
                                l = 0
                            syns = l
                            s = sl[l]
                            del sl,l
                            try:
                                pl = get_pkg_index(s)
                            except rq.ReadTimeout:
                                print(errormsg%("连接超时。",s,"请更换源或检查网络连接。"))
                            else:
                                try:
                                    pl = pl[tmp]
                                except:
                                    del s,syns
                                    print(errormsg%("错误，以下名称的软件包未找到：",tmp,"请检查是否输入正确！"))
                                else:
                                    l = []
                                    for i in list(pl.keys()):
                                        l.append(i)
                                    for i in range(len(l)):
                                        print("[%s] %s"%(i,l[i]))
                                    ttmp = input("请选择其中一个版本进行下载（默认为第一个）:\n?.>")
                                    try:
                                        ttmp = int(ttmp)
                                    except:
                                       ttmp = 0
                                    ttmp = l[ttmp]
                                    versionp = ttmp
                                    del l,ttmp,s
                                    ins_pkg(name=tmp,versionp=versionp,syns=syns)
                        case "注册":
                            pass
                        case "启动":
                            pass
                        case "信息":
                            pass
                        case "列表":
                            pass
                        case "关闭":
                            pass
                        case "卸载":
                            pass
                        case _:
                            print(errormsg%("“包”指令找不到以下参数：",inpl[1],"请检查您是否输入正确。"))
                case "帮助":
                    if inp == "帮助":
                        print(helps)
                    else:
                        print(errormsg%("意外地：",inp,"“帮助”命令没有参数。"))
                case "关于":
                    if inp == "关于":
                        try:
                            theads.append(threading.Thread(target=about,args=(version,"%s\n%s\n"%(version,copyright))))
                            theads[-1].start()
                        except:
                            pass
                        print("%s\n%s\n"%(version,copyright))
                    else:
                        print(errormsg%("意外地：",inp,"“关于”命令没有参数。"))
                case "清屏":
                    if inp == "清屏":
                        if sys.platform == "win32":
                            os.system("cls")
                        else:
                            os.system("clear")
                    else:
                        print(errormsg%("意外地：",inp,"“清屏”命令没有参数。"))
                case "退出":
                    if inp == "退出":
                        break
                    else:
                        print(errormsg%("意外地：",inp,"“退出”命令没有参数。"))
                case _:
                    print("[提示] %s正在自动调用系统命令行。\n\n"%project_name)
                    os.system(inp)

if __name__ == "__main__":
    main()