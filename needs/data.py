author = "DashBing(大师)"
copyright = "(c) %s 保留所有权利"%author
version_class = "Alpha"
resource_code = "1"
version_code = "3.2.7"
project_name = "DashShell"
if version_class == "GM":
    version = "%s v%s %s"%(project_name,version_code,version_class)
else:
    version = "%s v%s %s%s"%(project_name,version_code,version_class,resource_code)

preprint = """%s

%s
注:键入<帮助>可获得帮助

"""%(version,copyright)
helps = """[帮助]
帮助\t#获取帮助
关于\t#获取关于信息
清屏\t#清除屏幕中的字符
进入 [目录路径]\t#进入目录
    cd\t#简化版本 方法同上
包 <命令> [参数]\t#管理程序包
    安装 [包名]\t#从软件包仓库下载一个包并注册
    注册 [包文件名]\t#注册一个包
    启动 [包名]\t#启动一个包
    信息 [包名]\t#查看一个包的详细信息
    列表\t#查看已注册的包列表
    关闭 [包名]\t#强制关闭一个包
    卸载 [包名]\t#卸载一个包
退出  #退出程序

注：更多其他命令调用的是系统命令行，请键入<help>以获取帮助"""
errormsg = '''错误：%s
"%s"
%s
'''
