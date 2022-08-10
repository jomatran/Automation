from time import sleep
import logging
from util import list_entries, delete_file, check_file_type
from constant import IMAGE_EXTENSIONS

PATH = "/Users/haitran/Desktop/temp"


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    with list_entries(PATH) as entries:
        for entry in entries:
            name = entry.name
            if check_file_type(name, IMAGE_EXTENSIONS):
                delete_file(entry)
                sleep(1)
