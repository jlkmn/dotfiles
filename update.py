import os
from pathlib import Path
import shutil

files = [
            "Code/User/settings.json",
            "i3/config",
            "i3status/config"
        ]

def main():
    current_dir = os.getcwd()
    home_dir = Path.home()

    for f in files:
        shutil.copyfile(Path(home_dir, ".config", f), Path(current_dir, f))

if __name__ == '__main__':
    main()