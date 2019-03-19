#!/usr/bin/python
# -*- coding: utf-8 -*-
import cx_Freeze
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = "Win32GUI"  # pour application graphique sous Windows
#base = "Console" # pour application en console sous Windows



executables = [cx_Freeze.Executable("GUI\main.py",
                                   base=base,
                                   targetName="nombreejecutable.exe")]


build_exe_options = {"packages": ['time', 'sys', 'sqlite3', 'datetime', 'os', 'typing'],
                     "include_files":["DB",
                                     "GUI",
                                     "logica",
                                     "venv",
                                      os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                                      os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                                      ]}

cx_Freeze.setup(
    name="Alexito",
    version="1.0",
    description="esto es una prueba",
    options={"build_exe": build_exe_options},
    executables=executables
 )