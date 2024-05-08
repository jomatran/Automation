""""""

import json
import logging
import sys
import time

from src.utils.constant import DATE_TIME_FORMAT


class JSONFormatter:
    """A formatter for the standard logging module that converts a LogRecord into JSON

    Output matches JSONLayout from https://github.com/kdgregory/log4j-aws-appenders. Any
    keyword arguments supplied to the constructor are output in a "tags" sub-object.
    """

    def format(self, record):
        """
        Dumps json for log format
        """
        result = {
            "timestamp": time.strftime(DATE_TIME_FORMAT),
            "level": record.levelname,
            "logger": record.name,
            "message": record.msg % record.args,
            #     'hostname':     platform.node(),
            #     'processId':    record.process,
            #     'thread':       record.threadName,
            #     'locationInfo': {
            #         'fileName':     record.filename,
            #         'lineNumber':   record.lineno
            #     }
            # }]
        }
        return json.dumps(result)


def configure_logging():
    """Configure logging"""
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(JSONFormatter())
    logging.basicConfig(level=logging.INFO, handlers=[handler])
