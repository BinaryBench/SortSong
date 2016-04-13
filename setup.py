import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = []

setup(
      name="Moo",
      version="0.1",
      description="Mooing Many Moos",
      options={"build_exe": {"includes": includes}},
      executables=[Executable("SortSong.py", base=base)]
      )
