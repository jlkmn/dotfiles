from dataclasses import dataclass
from enum import Flag

class OS(Flag):
    WIN = 1
    LINUX = 2
    OSX = 4

@dataclass
class ConfigFile:
    osx_path: str = ""
    win_path: str = ""
    linux_path: str = ""
    os: OS = OS.WIN | OS.LINUX | OS.OSX