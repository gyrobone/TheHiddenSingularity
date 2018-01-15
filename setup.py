from cx_Freeze import *
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\Waylon Troyer\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Waylon Troyer\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

setup(
    name="TheHiddenSingularity-old",
    version="0.1",
    options={'build_exe': {'packages': ['pygame']}},
    executables=[
        Executable(
            "game.py",

        )
    ]
)
