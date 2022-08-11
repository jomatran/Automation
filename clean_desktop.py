from automation.handlers.move_handler import FileHandler
import time
import logging
from watchdog.observers import Observer
from automation.utils.injection import get_logger

if __name__ == "__main__":
    get_logger()
    desktop_path = "/Users/haitran/Desktop"
    handler = FileHandler(source=desktop_path)
    handler.clean_current()
    event_handler = handler
    observer = Observer()
    observer.schedule(event_handler, desktop_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
