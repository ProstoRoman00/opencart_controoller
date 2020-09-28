import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ['OpenCart','numpy','pandas','json','re'], "includes": ["PyQt5"], "excludes": ["tkinter"]}

setup(
    name='OpenCart',
    version='0.1',
    description='Program for OpenCart automation',
    author='ProstoRoman00',
    author_email='nestorukroma@gmail.com',
    options={"build_exe":build_exe_options},
    executables = [Executable("main.py",base="Win32GUI")]
)
