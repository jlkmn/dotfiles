import os
from pathlib import Path
import shutil
from typing import List
import logging
from sys import platform
from os import path

from dotmanage.models.ConfigFile import OS, ConfigFile
from dotmanage.fs import copy_files

config_files: List[ConfigFile] = [
    ConfigFile("/Users/{user}/Library/Application Support/Code/User/settings.json"),
    ConfigFile("/Users/{user}/Library/Application Support/Code/User/keybindings.json"),
    ConfigFile("/Users/{user}/Library/Fonts/Fura Mono Medium Nerd Font Complete.otf"),
    ConfigFile("/Users/{user}/.tmux.conf"),
    ConfigFile("/Library/Keyboard Layouts/Deutsch - Programming.icns", os=OS.OSX),
    ConfigFile("/Library/Keyboard Layouts/Deutsch - Programming.keylayout", os=OS.OSX),
]


def get(user="kul"):
    """
    Replaces files in .config with files from current system
    """
    logging.info("Importing system config")
    if platform == "darwin":
        for config_file in config_files:
            if not config_file.os & OS.OSX:
                continue
            full_path = config_file.osx_path.format(user=user)
            destination_path = f"./configfiles/{config_file.osx_path}"
            copy_files(Path(full_path), Path(destination_path))
    elif platform == "win32":
        for config_file in config_files:
            if not config_file.os & OS.WIN:
                continue
        pass


def set(user="kul"):
    """
    Replaces system files with files from .config
    """
    logging.info("Exporting config to system")
    if platform == "darwin":
        for config_file in config_files:
            if not config_file.os & OS.OSX:
                continue
            source_path = f"./configfiles/{config_file.osx_path}"
            destination_path = config_file.osx_path.format(user=user)
            copy_files(Path(source_path), Path(destination_path))
    elif platform == "win32":
        # Handle windows
        pass
