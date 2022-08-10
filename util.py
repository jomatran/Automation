import os
import shutil
from datetime import datetime
import re
from pathlib import Path
from constant import SCREENSHOT_PATH, IMAGE_EXTENSIONS, PY_EXTENSIONS, PYTHON_PATH, YAML_EXTENSIONS, YAML_PATH, DEFAULT, IGNORE_FILE
import logging


def move_file(entry, dest: str, file_name: str):
    Path(dest).mkdir(parents=True, exist_ok=True)
    file_exist = os.path.exists(dest+"/" + file_name)
    if file_exist:
        unique_file_name = make_unique(file_name)
        os.rename(entry, unique_file_name)
    if entry.is_file() and entry.name !=".DS_STORE":
        logging.info(f"Move file {file_name} to {dest}")
        shutil.move(entry, dest)


def delete_file(path):
    os.remove(path)


def make_unique(file_name: str):
    dt = datetime.now()
    ts = str(int(datetime.timestamp(dt)))
    return file_name + "_"+ts


def list_entries(src: str):
    return os.scandir(src)


def check_file_type(file_name: str, regex: str) -> bool:
    ext = os.path.splitext(file_name)[1]
    return ext is not None and re.match(regex, str(ext)) is not None


def get_path_by_type(file_name: str) -> str:
    if check_file_type(file_name, IMAGE_EXTENSIONS):
        return SCREENSHOT_PATH + "/"+str(datetime.date(datetime.now()))
    if check_file_type(file_name, PY_EXTENSIONS):
        return PYTHON_PATH
    if check_file_type(file_name, YAML_EXTENSIONS):
        return YAML_PATH
    return DEFAULT