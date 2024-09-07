"""
A class that gonna return the path and file name for image.
That will be seperated by date
"""

from datetime import datetime
from os.path import getctime

from src.design_patterns.factory.category import ICategory
from src.utils.common_functions import get_file_name_from_path
from src.utils.constant import DATE_FORMAT, IMAGE_PATH


class Image(ICategory):
    """
    Build path for image item
    """

    def get_path(self, source_file: str) -> str:
        result = IMAGE_PATH
        created_date = datetime.fromtimestamp(getctime(source_file)).strftime(
            DATE_FORMAT
        )
        result = IMAGE_PATH + "/" + created_date
        return result

    def modified_file_name(self, source_file: str) -> str:
        return get_file_name_from_path(source_file=source_file)
