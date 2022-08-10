from importlib.resources import path
import os
import shutil
from datetime import datetime
import re
from pathlib import Path
import logging


def move_file(entry, dest: str):
    Path(dest).mkdir(parents=True, exist_ok=True)
    file_exist = os.path.exists(dest+"/" + entry.name)
    if file_exist:
        unique_file_name = make_unique(entry.name)
        os.rename(entry, unique_file_name)
    if entry.is_file() and entry.name not in IGNORE_FILE:
        logging.info(f"Move file {entry.name} to {dest}")
        shutil.move(entry, dest)


def delete_file(entry):
    logging.info(f"Deleting file {entry.name}")
    os.remove(entry.path)


def make_unique(file_name: str):
    dt = datetime.now()
    ts = str(int(datetime.timestamp(dt)))
    return file_name + "_"+ts


def list_entries(src: str):
    return os.scandir(src)


def check_file_type(file_name: str, regex: str) -> bool:
    ext = os.path.splitext(file_name)[1]
    return ext is not None and re.match(regex, str(ext)) is not None
