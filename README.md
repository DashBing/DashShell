# DashShell
### *一个易用的中文命令行工具*
### 本项目由Python3.11环境下编写，资源在该环境下编译
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
### 说明文档语言仅支持简体中文

# 项目链接
[Github](https://github.com/DashBing/DashShell/ "Github")
<br><br>
[Kgithub](https://kgithub.com/DashBing/DashShell/)：国内Github镜像站，可能会有延迟，推送请使用Github链接推送

# 版本
## 稳定版本
+ 暂无

## 最新稳定版本
+ 暂无

## 最新正式版本
### *(master分支下数据不准确, 具体查看dev分支)*
+ v3.2.7-alpha1

# 从源码构建
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
#### *更改项目文件后具体参数请修改Makefile中的参数*

## 编译之前的准备工作
### 如果是在编译一次后再次进行编译
### 请用以下命令清理前一次编译的结果，或者可以考虑手动清除
```
make clean
```
### 在某些特殊情况下可能无法有效完全清除
### 请检查是否完全清除，若没有，请手动清除

## 生成目录以及独立的运行文件
### 使用
```
make
```
### 或者
```
make build
```
## 使用推荐选项生成资源（推荐）
### 该设置实际见生成定向打包的资源
### 生成目录
```
make dir
```
### 生成独立文件
```
make onefile
```
### 生成过程中产生的中间文件会自动清理
## 生成全编译的资源
### 即所有文件均编译为C并打包
### 生成目录
```
make static_dir
make clear_dir
```
### 生成独立文件
```
make static_onefile
make clear_onefile
```
### 第二行命令目的为清理编译过程中产生的中间文件以及整理编译结果

## 生成自动编译的资源
### 即自动打包文件(不推荐,可能会造成代码泄露)
### 生成目录
```
make auto_dir
make clear_dir
```
### 生成独立文件
```
make auto_onefile
make clear_onefile
```
### 第二行命令目的为清理编译过程中产生的中间文件以及整理编译结果

## 生成定向打包的资源
### 即设定好一部分编译为C，一部分直接打包
### 编译速度和安全兼顾
### 但是在修改文件内容后需要在Makefile中修改参数
### 生成目录
```
make zip_dir
make clear_dir
```
### 生成独立文件
```
make zip_onefile
make clear_onefile
```
### 第二行命令目的为清理编译过程中产生的中间文件以及整理编译结果

## 生成依赖于python的资源
### 不推荐，但是在前面几种出错后可以用这个
### 不会保护代码安全
### 生成目录
```
make vm_dir
make clear_dir
```
### 生成独立文件
```
make vm_onefile
make clear_onefile
```
### 第二行命令目的为清理编译过程中产生的中间文件以及整理编译结果
