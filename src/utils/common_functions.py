"""
Common functions that will use to another module
"""

from os import listdir
from os.path import splitext, join, isfile, exists
from re import match
from pathlib import Path
import logging
from src.utils.constant import IGNORE_FILE, FILE_NAME, DESTINATION


def is_expect_type(file_name: str, regex: str) -> bool:
    """
    Check extension of file name that depend on regex
    Args:
         file_name(str): Name of file
         arg2 (type): Regex of file extension
    Returns:
         Return true/false

    """
    ext = splitext(file_name)[1]
    return ext is not None and match(regex, str(ext)) is not None


def get_file_name_from_path(source_file: str) -> str:
    """
    Return file name from path
    Args:
        source_file (str): path of file
    Returns:
        File name
    """
    result = ""
    file_name_search = match(pattern=FILE_NAME, string=source_file)
    if file_name_search:
        logging.debug("Getting file name from %s", source_file)
        result = file_name_search.group(2)
        logging.debug("File name: %s", result)
    return result


def list_all_entry_from_path(source_dir: str) -> list[str]:
    """
    List all file from path
    Argr:
        source_dir (str): path
    Returns:
        List of entry
    """
    logging.info("List on file from source: %s", source_dir)
    return [
        join(source_dir, f)
        for f in listdir(source_dir)
        if isfile(join(source_dir, f)) and f not in IGNORE_FILE
    ]
