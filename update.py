import os
from pathlib import Path
import shutil

files = [
            ".config/Code/User/settings.json",
            ".config/i3/config",
            ".config/i3status/config",
        ]


def replace_dots(s):
    return "/".join(s.split("/")[:-1]).replace(".", "dot")

def main():
    current_dir = os.getcwd()
    home_dir = Path.home()

    print("Copying files")
    for f in files:
        src_path = Path(home_dir, f)
        destination_dir = replace_dots(f)
        destination_file = src_path.name
        dst_path = Path(current_dir, f"{destination_dir}/{destination_file}")
        os.makedirs(destination_dir, exist_ok=True)
        shutil.copyfile(src_path, dst_path)

if __name__ == '__main__':
    main()