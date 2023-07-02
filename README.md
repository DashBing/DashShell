# DashShell
### *一个易用的中文命令行工具*
### 本项目由Python3.11环境下编写，资源在该环境下编译
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
### 说明文档语言仅支持简体中文

# 项目链接
[Github](https://github.com/DashBing/DashShell/ "Github")
<br><br>
[Kgithub](https://kgithub.com/DashBing/DashShell/)：国内Github镜像站，可能会有延迟，推送请使用Github链接推送

# 从源码构建
### 注意：本项目并非跨平台，仅支持在Windows平台下运行
## 准备工作
+ 安装git和make (方法自行百度)
+ 安装Python(3.9版本或者3.11版本皆可)
+ 从源码仓库克隆源代码
```
git clone git@github.com:DashBing/DashShell.git
```
#### 或者
```
git clone https://github.com/DashBing/DashShell.git
```
### 国内网比较差可以尝试：
```
git clone https://kgithub.com/DashBing/DashShell.git
```

## 初始化打包环境
### 注意，如果你已经安装nuitka了请不要使用以下命令
```
make init
```
#### 或者
#### 尝试手动安装以下包:
+ nuitka (作者编译环境的版本号为1.5.3)

## 构建项目
### 生成目录以及独立的运行文件
#### 使用
```
make
```
#### 或者
```
make build
```
### 使用推荐选项生成资源（推荐）
#### 生成目录
```
make dir
```
#### 生成独立文件
```
make onefile
```
#### 生成过程中产生的中间文件会自动清理
### 生成全编译的资源
#### 即所有文件均编译为C并打包
#### 生成目录
```
make static_onefile
```
#### 生成独立文件
