from cx_Freeze import setup, Executable

exe = Executable(
     script="SortSong.py",
     base="Win32Gui",
     icon="Icon.ico"
     )
includefiles = []
includes = []
excludes = []
packages = ["os", "re", "shutil", "sys", "getopt", "mutagen.easyid3"]

setup(
     version="0.0",
     description="No Description",
     author="Name",
     name="App name",
     options={'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
     executables=[exe]
     )
