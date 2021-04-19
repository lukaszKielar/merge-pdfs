import sys

from cx_Freeze import Executable, setup

base = "Win32GUI" if sys.version == "win32" else None

setup(
    name="merge_pdfs",
    version="0.0.1",
    author="Lukasz Kielar",
    description="Tool for merging PDF files without sending them over the Network",
    executables=[Executable("merge_pdfs/gui/app.py", base=base)],
)
