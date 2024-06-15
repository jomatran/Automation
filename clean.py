"""
Main file to run program
"""

# import time
# from watchdog.observers import Observer
from src.injections.log import configure_logging
from src.handlers.file_hanlder import FileHandler
from src.utils.constant import DESKTOP_PATH

if __name__ == "__main__":
    configure_logging()
    file_hanlder = FileHandler(source=DESKTOP_PATH)
    file_hanlder.clean_current()
    # event_handler = file_hanlder
    # observer = Observer()
    # observer.schedule(event_handler, DESKTOP_PATH, recursive=True)
    # observer.start()
    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    # observer.join()
