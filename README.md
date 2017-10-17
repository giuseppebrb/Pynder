# Pynder

## Important Disclaimer
Pynder was **NOT** created with any malicious purpose.
The source code is only reported for study purposes and didactics.
The author condemns the use of code for criminal purposes and any
action that violates what is said will have to be pursued in the direct confrontations of those responsible.

### What Is It?
Pynder is a python script that allows you to search and send, by email, all the files corresponding to a particular model 
that are located inside the computer where it is run.
For example, by setting the search pattern as _"*.pdf"_ or _"*.doc"_ all files of these extensions on the computer will 
be sent directly to the selected email address.


You can further refine the search to "IMG-*.jpg" as follows. 
This will only email files with extension .jpg whose name begins with IMG-.

Pynder at the first run copy itself into another folder and auto-launch from there so that the POTENTIAL victim can
delete the executable that he launched without compromising the whole process.
Pynder runs totally in the background, so once you run, there are no windows or visible icons.

### How To Compile It
If you intend to create a single standalone executable file, without python being necessarily installed on the machine,
you can use one of the following methods.
On Windows:
- pyinstaller
- py2exe

On MacOS:
- py2app

#### pyinstaller
PyInstaller is a program that freezes (packages) Python programs into stand-alone executables, under Windows, Linux, Mac OS X, FreeBSD, Solaris and AIX. Its main advantages over similar tools are that PyInstaller works with Python 2.7 and 3.3—3.6, it builds smaller executables thanks to transparent compression, it is fully multi-platform, and use the OS support to load the dynamic libraries, thus ensuring full compatibility. (from: http://www.pyinstaller.org/)

After installing pyinstaller, open the command prompt, navigate to the script folder, and type the following command:
`pyinstaller -w --onefile finder.py`
or
`pyinstaller -w --onefile --icon=icon.ico finder.py`  if you want to create an executable with a custom icon.

#### py2exe
py2exe is a Python Distutils extension which converts Python scripts into executable Windows programs, able to run without requiring a Python installation. (from: http://www.py2exe.org/)

After installing py2exe, open the command prompt, navigate to the script folder, and type the following command:
`python setup.py py2exe`

#### py2app
py2app is a Python setuptools command which will allow you to make standalone application bundles and plugins from Python scripts. py2app is similar in purpose and design to py2exe for Windows. (from: https://py2app.readthedocs.io/en/latest/)

After installing py2app, open the command prompt, navigate to the script folder, and type the following command:
`python setup.py py2app`