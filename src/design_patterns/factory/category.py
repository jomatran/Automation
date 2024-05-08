"""
An class that represent a factory design pattern
"""

from abc import ABCMeta, abstractmethod


class ICategory(metaclass=ABCMeta):
    """
    An interface that will be a place where you can put your method
    over here if you want to implement by category
    """

    @abstractmethod
    def get_path(self, source_file: str) -> str:
        """
        Get destination base on kile extension
        Args:
            source_file (str): source file
        Returns:
            Destination path for file
        """

    @abstractmethod
    def modified_file_name(self, source_file: str) -> str:
        """
        Changing file name based on type if need it
        Args:
            source_file (str): file name string
        Returns:
            File name that was modified
        """
