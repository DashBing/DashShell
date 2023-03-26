## 常量
PJNAME := DashShell
NEEDDIR := needs
NUITKA := nuitka
MAINNAME := main
ICON := icon.ico
COMPILE := --clang

DIRNAME := $(PJNAME).dist
MAINFILE := $(MAINNAME).py

ifeq ($(OS),Windows_NT)
	ICONBASH := --windows-icon-from-ico=$(ICON)
	RMDIR := rmdir /s /q
	FILENAME := $(PJNAME).exe
	RM := del /q
else
	RMDIR := rmdir -rf
#ifeq ($(shell uname),Darwin)
#	ICONBASH := --macos-app-icon=$(ICON)
#else
	ICONBASH := --linux-icon=$(ICON)
	FILENAME := $(PJNAME)
	RM := rm -f
#endif
endif


## 其他编译选项区
all:
	make onefile
	make dir
	make clear

init:
	python -m pip install -U "nuitka>=1.0.6"

dir:
	make zip_dir

onefile:
	make zip_onefile

clear:
	$(RMDIR) $(MAINNAME).build
	$(RMDIR) $(MAINNAME).dist
	$(RMDIR) $(MAINNAME).onefile-build
#mv -r $(DIRNAME)/$(MAINNAME).dist ./$(PJNAME)
#$(RMDIR) $(DIRNAME)
	cd $(DIRNAME)
	$(RMDIR) $(MAINNAME).build

clean:
	$(RMDIR) $(DIRNAME)
	$(RM) $(FILENAME)

rm:
	make clear
	make clean

## 编译选项区
# 静态打包编译
static_onefile:
	$(NUITKA) --standalone $(COMPILE) --follow-imports --onefile --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

static_dir:
	$(NUITKA) --standalone $(COMPILE) --follow-imports --output-filename="$(FILENAME)" --output-dir="$(DIRNAME)" $(ICONBASH) $(MAINFILE)

# 自动打包编译
auto_onefile:
	$(NUITKA) --standalone $(COMPILE) --onefile --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

auto_dir:
	$(NUITKA) --standalone $(COMPILE) --output-filename="$(FILENAME)" --output-dir="$(DIRNAME)" $(ICONBASH) $(MAINFILE)

# 动态打包编译
zip_onefile:
	$(NUITKA) --standalone $(COMPILE) --onefile --nofollow-imports --follow-import-to=$(NEEDDIR) --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

zip_dir:
	$(NUITKA) --standalone $(COMPILE) --nofollow-imports --follow-import-to=$(NEEDDIR) --output-filename="$(FILENAME)" --output-dir="$(DIRNAME)" $(ICONBASH) $(MAINFILE)

# 依赖Python运行时的编译
vm_onefile:
	$(NUITKA) --onefile $(COMPILE) --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

vm_dir:
	$(NUITKA) $(COMPILE) --output-filename="$(FILENAME)" --output-dir="$(DIRNAME)" $(ICONBASH) $(MAINFILE)
