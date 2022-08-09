import os
from pathlib import Path
import shutil

class DotFile:
    def __init__(self, position, name):
        self.position = position
        self.name = name

files = [
            DotFile(".config", "Code/User/settings.json"),
            DotFile(".config", "i3/config"),
            DotFile(".config", "i3status/config")
        ]

def main():
    current_dir = os.getcwd()
    home_dir = Path.home()

    print("Copying files")
    for f in files:
        shutil.copyfile(Path(home_dir, f.position, f.name), Path(current_dir, f.name))

if __name__ == '__main__':
    main()