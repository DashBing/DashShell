## 常量
PJNAME := DashShell
NEEDDIR := needs
NUITKA := nuitka
MAINNAME := main
ICON := icon.ico

DIRNAME := $(PJNAME).dist
FILENAME := $(PJNAME).exe
MAINFILE := $(MAINNAME).py

ifeq ($(OS),Windows_NT)
	ICONBASH := --windows-icon-from-ico=$(ICON)
	RMDIR := rmdir /s /q
else
	RMDIR := rmdir -rf
#ifeq ($(shell uname),Darwin)
#	ICONBASH := --macos-app-icon=$(ICON)
#else
	ICONBASH := --linux-icon=$(ICON)
#endif
endif
## 编译选项区
# 静态打包编译
static_onefile:
	$(NUITKA) --standalone --follow-imports --onefile --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

static_dir:
	$(NUITKA) --standalone --follow-imports --output-filename="$(FILENAME)" --output-dir="$(DIRNAME)" $(ICONBASH) $(MAINFILE)

# 自动打包编译
auto_onefile:
	$(NUITKA) --standalone --onefile --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

auto_dir:
	$(NUITKA) --standalone --output-filename="$(FILENAME)" --output-dir="$(DIRNAME)" $(ICONBASH) $(MAINFILE)

# 动态打包编译
zip_onefile:
	$(NUITKA) --standalone --onefile --nofollow-imports --follow-import-to=$(NEEDDIR) --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

zip_dir:
	$(NUITKA) --standalone --nofollow-imports --follow-import-to=$(NEEDDIR) --output-filename="$(FILENAME)" --output-dir="$(DIRNAME)" $(ICONBASH) $(MAINFILE)

# 依赖Python运行时的编译
vm_onefile:
	$(NUITKA) --onefile --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

vm_dir:
	$(NUITKA) --output-filename="$(FILENAME)" --output-dir="$(DIRNAME)" $(ICONBASH) $(MAINFILE)


## 其他编译选项区

init:
	python -m pip install -U "nuitka>=1.0.6"

dir:
	make auto_dir

onefile:
	make auto_onefile

clear:
	$(RMDIR) $(MAINNAME).build
	$(RMDIR) $(MAINNAME).dist
	$(RMDIR) $(MAINNAME).onefile-build
#mv -r $(DIRNAME)/$(MAINNAME).dist ./$(PJNAME)
#$(RMDIR) $(DIRNAME)
	$(RMDIR) $(DIRNAME)/$(MAINNAME).build

all:
	make init
	make onefile
	make dir
	make clear