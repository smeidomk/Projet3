from cx_Freeze import setup, Executable


executables = [Executable("launchgame.py")]
includefiles = ["images", "labyrinth.py", "constants.py", "macgyver.py", "main.py"]
packages = ["pygame"]

options = {
            "include_files": includefiles,
            "packages": packages,
          }

setup(
    name = "MacGyver",
    version = "1.0",
    options = {"build_exe": options},
    description = "L'aventure de MacGyver",
    executables = executables
)
