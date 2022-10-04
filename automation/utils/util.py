import logging
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

from automation.utils.constant import IGNORE_FILE


def move(entry, dest: str):
    Path(dest).mkdir(parents=True, exist_ok=True)
    file_exist = os.path.exists(dest+"/" + entry.name)
    if file_exist:
        logging.warn(f"{entry.name} already exist in {dest}")
        unique_file_name = entry.name+ "_"+str(int(datetime.timestamp(datetime.now())))
        logging.warn(f"changing name from {entry.name} to {unique_file_name}")
        os.rename(entry, unique_file_name)
    logging.info(f"=================>MOVING {entry.name} TO {dest}<=================")
    shutil.move(entry, dest)
    logging.info(f"=================>MOVED {entry.name} TO {dest}<=================\n")



def delete_file(entry):
    if entry.is_file() and entry.name not in IGNORE_FILE:
        logging.info(f"=================>Deleting file {entry.name}<=================")
        shutil.rmtree(entry.path)
        logging.info(f"=================>Deleted file {entry.name}<=================\n")


def list_entries(src: str):
    return os.scandir(src)


def is_expect_type(file_name: str, regex: str) -> bool:
    ext = os.path.splitext(file_name)[1]
    return ext is not None and re.match(regex, str(ext)) is not None
