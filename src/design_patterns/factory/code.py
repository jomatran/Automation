"""
A class that gonna return the path and file name for code files. Such as java, python, etc
"""

from os.path import splitext
from src.design_patterns.factory.category import ICategory
from src.utils.constant import CODE_PATH
from src.utils.common_functions import get_file_name_from_path


class Code(ICategory):
    """
    Build path for code item
    """

    def get_path(self, source_file: str) -> str:
        result_path = CODE_PATH
        file_name = get_file_name_from_path(source_file=source_file)
        if file_name.lower().startswith("docker"):
            result_path = f"{CODE_PATH}/docker"

        file_name_prefix, file_ext = splitext(file_name)
        if file_ext:
            extension_mapping = {
                ".py": "python",
                ".json": "json",
                ".yaml": "yaml",
                ".sh": "sh",
            }
            result_path = f"{CODE_PATH}/{extension_mapping.get(file_ext, '')}"

        return result_path

    def modified_file_name(self, source_file: str) -> str:
        return get_file_name_from_path(source_file=source_file)
