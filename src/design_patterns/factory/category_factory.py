"""
A factory class that will return a specific class which will corresponding with file extension
"""

import logging
from src.design_patterns.factory.category import ICategory
from src.design_patterns.factory.code import Code
from src.design_patterns.factory.micorsoft import Microsoft
from src.design_patterns.factory.image import Image
from src.design_patterns.factory.other import DefaultHandler
from src.utils.common_functions import is_expect_type, get_file_name_from_path
from src.utils.constant import (
    IMAGE_EXTENSIONS,
    YAML_EXTENSIONS,
    PY_EXTENSIONS,
    SH_EXTENSIONS,
    MS_EXTENSION,
)


class CategoryFactory:
    @staticmethod
    def type_factory(source_file: str) -> ICategory:
        """
        A factory method that will return an object
        """
        result = DefaultHandler()
        file_name = get_file_name_from_path(source_file=source_file)
        if is_expect_type(file_name=file_name, regex=IMAGE_EXTENSIONS):
            logging.debug("Get image handling")
            result = Image()
        if (
            is_expect_type(file_name=file_name, regex=PY_EXTENSIONS)
            or is_expect_type(file_name=file_name, regex=SH_EXTENSIONS)
            or is_expect_type(file_name=file_name, regex=YAML_EXTENSIONS)
            or file_name.lower().startswith("docker")
        ):
            logging.debug("Get code handling")
            result = Code()
        if is_expect_type(file_name=file_name, regex=MS_EXTENSION):
            logging.debug("Get microsoft handling")
            result = Microsoft()
        return result
