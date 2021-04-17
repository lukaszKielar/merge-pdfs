from cx_Freeze import Executable, setup

setup(
    name="MergePDFs",
    version="0.0.1",
    author="Lukasz Kielar",
    description="Tool for merging PDF files without sending them over the Network",
    executables=[Executable("merge_pdfs/gui/app.py", base="Win32GUI")],
)
