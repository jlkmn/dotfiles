from typing import List
import logging

from dotmanage.models.ConfigFile import ConfigFile

files: List[ConfigFile] = [
        ConfigFile("~/.config/nvim/init.lua", "")
    ]

def get():
    """
    Replaces files in .config with files from current system
    """
    for file in files:
        logging.info(file.osx_path)

def set():
    """
    Replaces system files with files from .config
    """
    logging.info("HI")