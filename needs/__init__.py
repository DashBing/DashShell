import os
import sys
from json import dumps as jen
from json import dumps as jde
from .data import errormsg,helps,preprint,version,author
from .commands import init_pkgindex,about
import threading

def main():
    print(preprint)
    init_pkgindex()
    pkg_theads = {}
    theads = []
    while True:
        inp = input("%s>"%os.getcwd())
        if inp != "":
            inpl = inp.split(" ")
            match inpl[0]:
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
                        case "注册":
                            pass
                        case "启动":
                            pass
                        case "信息":
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
                            theads.append(threading.Thread(target=about,args=(version,author)))
                            theads[-1].start()
                        except:
                            print(copyright)
                    else:
                        print(errormsg%("意外地：",inp,"“关于”命令没有参数。"))
                case "清屏":
                    if inp == "清屏":
                        print("维护中...")#调用dll,暂空
                    else:
                        print(errormsg%("意外地：",inp,"“清屏”命令没有参数。"))
                case "退出":
                    if inp == "退出":
                        break
                    else:
                        print(errormsg%("意外地：",inp,"“退出”命令没有参数。"))
                case _:
                    print("[提示] DashShell正在自动调用系统命令行。")
                    os.system(inp)

if __name__ == "__main__":
    main()