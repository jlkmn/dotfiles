import os
import shutil
from typing import List
import logging
from sys import platform
from os import path

from dotmanage.models.ConfigFile import ConfigFile

config_files: List[ConfigFile] = [
        ConfigFile("/Users/kul/Library/Application Support/Code/User/settings.json", ""),
        ConfigFile("/Users/kul/Library/Application Support/Code/User/keybindings.json", ""),
    ]

def get():
    """
    Replaces files in .config with files from current system
    """
    if platform == "darwin":
        for config_file in config_files:
            logging.info("Getting %s", config_file.osx_path)
            full_path = config_file.osx_path

            if not path.exists(full_path):
                logging.warning("File does not exist on system")
                continue

            destination_path = f"./configfiles/{config_file.osx_path}"
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copy(full_path, destination_path)
    elif platform == "win32":
        # Handle windows
        pass
                

def set():
    """
    Replaces system files with files from .config
    """
    if platform == "darwin":
        for config_file in config_files:
            logging.info("Setting %s", config_file.osx_path)
            source_path = f"./configfiles/{config_file.osx_path}"

            if not path.exists(source_path):
                logging.warning("Does not exist in configfiles")
                continue

            os.makedirs(os.path.dirname(config_file.osx_path), exist_ok=True)
            shutil.copy(source_path, config_file.osx_path)
    elif platform == "win32":
        # Handle windows
        pass