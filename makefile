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
	RNM := ren
else
	RMDIR := rmdir -rf
	ICONBASH := --linux-icon=$(ICON)
	FILENAME := $(PJNAME)
	RM := rm -f
	RNM := mv
endif


## 其他编译选项区
build:
	make onefile
	make dir
#make clear

init:
	python -m pip install -U "nuitka>=1.0.6"

dir:
	make zip_dir
	make clear_dir

onefile:
	make zip_onefile
	make clear_onefile

clear_onefile:
	$(RMDIR) $(MAINNAME).build
	$(RMDIR) $(MAINNAME).dist
	$(RMDIR) $(MAINNAME).onefile-build

clear_dir:
	$(RMDIR) $(MAINNAME).build
	$(RNM) $(MAINNAME).dist $(PJNAME)

clear:
	make clear_dir
	make clear_onefile

clean:
	$(RMDIR) $(DIRNAME)
	$(RM) $(FILENAME)

rm:
	make clear
	make clean

## 编译选项区
# 静态打包编译
static_onefile:$(MAINFILE) $(NEEDDIR)
	$(NUITKA) --standalone $(COMPILE) --follow-imports --onefile --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

static_dir:$(MAINFILE) $(NEEDDIR)
	$(NUITKA) --standalone $(COMPILE) --follow-imports --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

# 自动打包编译
auto_onefile:$(MAINFILE) $(NEEDDIR)
	$(NUITKA) --standalone $(COMPILE) --onefile --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

auto_dir:$(MAINFILE) $(NEEDDIR)
	$(NUITKA) --standalone $(COMPILE) --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

# 动态打包编译
zip_onefile:$(MAINFILE) $(NEEDDIR)
	$(NUITKA) --standalone $(COMPILE) --onefile --nofollow-imports --follow-import-to=$(NEEDDIR) --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

zip_dir:$(MAINFILE) $(NEEDDIR)
	$(NUITKA) --standalone $(COMPILE) --nofollow-imports --follow-import-to=$(NEEDDIR) --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

# 依赖Python运行时的编译
vm_onefile:$(MAINFILE) $(NEEDDIR)
	$(NUITKA) --onefile $(COMPILE) --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)

vm_dir:$(MAINFILE) $(NEEDDIR)
	$(NUITKA) $(COMPILE) --output-filename="$(FILENAME)" $(ICONBASH) $(MAINFILE)
