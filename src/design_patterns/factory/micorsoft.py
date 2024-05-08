"""
A class that gonna return the path and file name for microsoft files
"""

from os.path import splitext
from os.path import getctime
from datetime import datetime
from src.design_patterns.factory.category import ICategory
from src.utils.constant import MS_PATH
from src.utils.common_functions import get_file_name_from_path
from src.utils.constant import DATE_FORMAT


class Microsoft(ICategory):
    """
    Build path for microsoft item
    """

    def get_path(self, source_file: str) -> str:
        result_path = MS_PATH
        file_name = get_file_name_from_path(source_file=source_file)
        if self.__is_catchup_file(file_name=file_name):
            result_path = MS_PATH + "/" + "catchup"
        return result_path

    def modified_file_name(self, source_file: str) -> str:
        file_name = get_file_name_from_path(source_file=source_file)
        if self.__is_catchup_file(file_name=file_name):
            file_name_prefix, file_ext = splitext(file_name)
            created_date = datetime.fromtimestamp(getctime(source_file)).strftime(
                DATE_FORMAT
            )
            file_name = file_name_prefix + "_" + created_date + file_ext

        return file_name

    def __is_catchup_file(self, file_name: str) -> bool:
        """
        Check is a catchup file
        Args:
            file_name (str): File name
        Returns:
            True/false
        """
        result = False
        if file_name:
            result = file_name.lower().startswith("catchup")
        return result
