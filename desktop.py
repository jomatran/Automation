from time import sleep
import logging
from watchdog.observers import Observer
from move_handler import MoverHandler

DESKTOP_PATH = "/Users/haitran/Desktop"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s — %(levelname)s — %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = DESKTOP_PATH
    handler = MoverHandler(path=DESKTOP_PATH)
    event_handler = handler
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        handler.clean_current()
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
