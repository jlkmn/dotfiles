import logging
import os
from pathlib import Path
import shutil

def save_copy(src_path, dst_path):
    logging.info("Copying: %s", src_path)
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    shutil.copy(src_path, dst_path)

def copy_files(src: Path, dst: Path, extra_path: str = ""):
    if not src.exists():
        logging.warning("File does not exist on system")
        return

    if not src.is_dir():
        save_copy(str(src), str(dst))
        return

    for item in src.iterdir():
        if item.is_dir():
            copy_files(item, dst, f"{extra_path}/{item.name}")
        else:
            save_copy(str(item), f"{dst}{extra_path}/{item.name}")