"""
Handling to move file
"""

import logging

from os import rename
from os.path import exists

from pathlib import Path
from watchdog.events import FileSystemEventHandler
from src.design_patterns.factory.category_factory import CategoryFactory
from src.utils.common_functions import list_all_entry_from_path


class FileHandler(FileSystemEventHandler):

    def __init__(self, source: str) -> None:
        self.__source = source

    def clean_current(self) -> None:
        """
        Clean all file which were existed on desktop
        """
        all_files = list_all_entry_from_path(source_dir=self.__source)
        for file in all_files:
            # logging.debug("Check %s exist", file)
            file_exist = exists(file)
            if file_exist:
                ct = CategoryFactory.type_factory(source_file=file)
                destination_folder = ct.get_path(source_file=file)
                file_name = ct.modified_file_name(source_file=file)
                Path(destination_folder).mkdir(parents=True, exist_ok=True)
                dest_file = f"{destination_folder}/{file_name}"
                logging.info("Moving %s to %s", file, dest_file)
                rename(file, dest_file)
