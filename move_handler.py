from time import sleep
import logging
from watchdog.events import FileSystemEventHandler
from util import list_entries, move_file, get_path_by_type



class MoverHandler(FileSystemEventHandler):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path


    def on_modified(self, event):
        with list_entries(self.path) as entries:
            for entry in entries:
                name = entry.name
                destination = get_path_by_type(name)
                move_file(entry, destination, name)


    def clean_current(self):
        logging.info(f"clean current path {self.path}")
        with list_entries(self.path) as entries:
            for entry in entries:
                if entry.is_file() and entry.name !=".DS_STORE":
                    name = entry.name
                    destination = get_path_by_type(name)
                    logging.info(f"Move file {name} to {destination}")
                    sleep(1)