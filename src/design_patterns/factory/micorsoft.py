"""
A class that gonna return the path and file name for microsoft files
"""

from datetime import datetime
from os.path import getctime, splitext

from src.design_patterns.factory.category import ICategory
from src.utils.common_functions import get_file_name_from_path
from src.utils.constant import DATE_FORMAT, MS_PATH


class Microsoft(ICategory):
    """
    Build path for microsoft item
    """

    def get_path(self, source_file: str) -> str:
        result_path = ""
        file_name = get_file_name_from_path(source_file=source_file)
        if self.__is_catchup_file(file_name=file_name):
            result_path = MS_PATH + "/" + "catchup"
        else:
            result_path = (
                MS_PATH + "/" + self.__seperate_folder_by_extension(file_name=file_name)
            )
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

    def __seperate_folder_by_extension(self, file_name: str) -> str:
        folder = {
            ".xlsx": "excel",
            ".docx": "docs",
            ".txt": "txt",
            ".doc": "docs",
            ".pptx": "pptx",
        }
        file_name_prefix, file_ext = splitext(file_name)
        return folder.get(file_ext, "")
