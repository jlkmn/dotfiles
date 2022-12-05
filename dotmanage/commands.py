import os
import shutil
from typing import List
import logging
from sys import platform
from os import path

from dotmanage.models.ConfigFile import OS, ConfigFile

config_files: List[ConfigFile] = [
        ConfigFile("/Users/{user}/Library/Application Support/Code/User/settings.json"),
        ConfigFile("/Users/{user}/Library/Application Support/Code/User/keybindings.json"),
        ConfigFile("/Users/{user}/Library/Application Support/Code/User/keybindings.json"),
        ConfigFile("/Users/{user}/.tmux.conf"),
        ConfigFile("/Library/Keyboard Layouts/Deutsch - Programming.icns", os=OS.OSX),
        ConfigFile("/Library/Keyboard Layouts/Deutsch - Programming.keylayout", os=OS.OSX),    ]

def get(user="kul"):
    """
    Replaces files in .config with files from current system
    """
    if platform == "darwin":
        for config_file in config_files:
            if not config_file.os & OS.OSX:
                continue
            full_path = config_file.osx_path.format(user=user)
            logging.info("Getting %s", full_path)

            if not path.exists(full_path):
                logging.warning("File does not exist on system")
                continue

            destination_path = f"./configfiles/{config_file.osx_path}"
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copy(full_path, destination_path)
    elif platform == "win32":
        for config_file in config_files:
            if not config_file.os & OS.WIN:
                continue
        pass
                

def set(user="kul"):
    """
    Replaces system files with files from .config
    """
    if platform == "darwin":
        for config_file in config_files:
            if not config_file.os & OS.OSX:
                continue
            logging.info("Setting %s", config_file.osx_path)
            source_path = f"./configfiles/{config_file.osx_path}"

            if not path.exists(source_path):
                logging.warning("Does not exist in configfiles")
                continue

            destination_path = config_file.osx_path.format(user=user)
            logging.info("Destination path: %s", destination_path)
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copy(source_path, destination_path)
    elif platform == "win32":
        # Handle windows
        pass
