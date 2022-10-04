from datetime import datetime
from watchdog.events import FileSystemEventHandler
from automation.utils.util import list_entries, move, is_expect_type
from automation.utils.constant import IGNORE_FILE, DEFAULT, IMAGE_EXTENSIONS, IMAGE_PATH, MS_EXTENSION, MS_PATH, PY_EXTENSIONS, PYTHON_PATH, JSON_EXTENSIONS, JSON_PATH, YAML_EXTENSIONS, YAML_PATH, SH_PATH, SH_EXTENSIONS
from abc import ABCMeta, abstractmethod
import time


class MoveHandler(metaclass=ABCMeta):
    def __init__(self, source: str) -> None:
        self.source = source

    @abstractmethod
    def clean_current(self) -> None:
        pass


class FileHandler(MoveHandler, FileSystemEventHandler):
    def __init__(self, source: str) -> None:
        super().__init__(source)

    def clean_current(self) -> None:
        # with list_entries(src=self.source) as entries:
        for entry in list_entries(src=self.source):
            if entry.is_file() and entry.name not in IGNORE_FILE:
                move(entry=entry, dest=self.build_path_from_type(entry.name))
                time.sleep(1)

    def on_modified(self, event):
        for entry in list_entries(src=self.source):
            if entry.is_file() and entry.name not in IGNORE_FILE:
                move(entry=entry, dest=self.build_path_from_type(entry.name))
                time.sleep(1)

    def build_path_from_type(self, name: str):
        path = DEFAULT
        if is_expect_type(name, IMAGE_EXTENSIONS):
            path = IMAGE_PATH + "/"+str(datetime.date(datetime.today()))
        if is_expect_type(name, MS_EXTENSION):
            path = MS_PATH
        if is_expect_type(name, PY_EXTENSIONS):
            path = PYTHON_PATH
        if is_expect_type(name, JSON_EXTENSIONS):
            path = JSON_PATH
        if is_expect_type(name, YAML_EXTENSIONS):
            path = YAML_PATH
        if is_expect_type(name, SH_EXTENSIONS):
            path = SH_PATH
        return path
