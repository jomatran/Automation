from time import sleep
import logging
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from util import list_entries, move_file, check_file_type
from constant import SCREENSHOT_PATH, IMAGE_EXTENSIONS, PY_EXTENSIONS, PYTHON_PATH, YAML_EXTENSIONS, YAML_PATH, DEFAULT, IGNORE_FILE, JSON_PATH, JSON_EXTENSIONS, SH_EXTENSIONS, SH_PATH, MS_EXTENSION, MS_PATH


class MoverHandler(FileSystemEventHandler):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path


    def on_modified(self, event):
        with list_entries(self.path) as entries:
            for entry in entries:
                destination = self.get_path_by_type(entry.name)
                move_file(entry, destination)


    def clean_current(self):
        logging.info(f"clean current path {self.path}")
        with list_entries(self.path) as entries:
            for entry in entries:
                destination = self.get_path_by_type(entry.name)
                move_file(entry,destination)
                sleep(1)


    def get_path_by_type(self,file_name: str) -> str:
        default_path = DEFAULT
        if check_file_type(file_name, IMAGE_EXTENSIONS):
            default_path = SCREENSHOT_PATH + "/"+str(datetime.date(datetime.now()))
        if check_file_type(file_name, PY_EXTENSIONS):
            default_path = PYTHON_PATH
        if check_file_type(file_name, YAML_EXTENSIONS):
            default_path= YAML_PATH
        if check_file_type(file_name, JSON_EXTENSIONS):
            default_path= JSON_PATH
        if check_file_type(file_name, SH_EXTENSIONS):
            default_path= SH_PATH
        if check_file_type(file_name, MS_EXTENSION):
            default_path= MS_PATH
        return default_path