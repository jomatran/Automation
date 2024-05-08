"""
A class that will handle for any file that does not category yet
"""

from src.design_patterns.factory.category import ICategory
from src.utils.common_functions import get_file_name_from_path
from src.utils.constant import DEFAULT


class DefaultHandler(ICategory):
    """
    A class that will handle for any file that does not category yet
    """

    def get_path(self, source_file: str) -> str:
        return DEFAULT

    def modified_file_name(self, source_file: str) -> str:
        return get_file_name_from_path(source_file=source_file)
