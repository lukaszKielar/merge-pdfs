import os
import sys

import PyQt5
from cx_Freeze import Executable, setup

base = "Win32GUI" if sys.version == "win32" else None
include_files = [
    os.path.join(os.path.dirname(PyQt5.__file__), "Qt5", "plugins"),
    "c:\windows\syswow64\MSVCR100.dll",
    "c:\windows\syswow64\MSVCP100.dll",
]

setup(
    name="merge_pdfs",
    version="0.0.1",
    author="Lukasz Kielar",
    description="Tool for merging PDF files without sending them over the Network",
    executables=[Executable("merge_pdfs/gui/app.py", base=base)],
    options={
        "build_exe": {
            "packages": ["PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets"],
            "include_files": include_files,
        }
    },
)
