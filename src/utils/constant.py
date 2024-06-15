"""
File extension regex
"""

# Path
DEFAULT = "/Users/haitran/Desktop/temp/other"
DESTINATION = "/Users/haitran/Desktop/temp"
MS_PATH = "/Users/haitran/Desktop/temp/ms"
IMAGE_PATH = "/Users/haitran/Desktop/temp/screenshot"
CODE_PATH = "/Users/haitran/Desktop/temp/code"
DESKTOP_PATH = "/Users/haitran/Desktop"

# Extension
IMAGE_EXTENSIONS = ".(?:gif|jpg|jpeg|tiff|png|GIF|JPG|JPEG|TIFF|PNG)"
YAML_EXTENSIONS = ".(?:yaml|yml)"
PY_EXTENSIONS = ".(?:py)"
SH_EXTENSIONS = ".(?:sh)"
JSON_EXTENSIONS = ".(?:json)"
IGNORE_FILE = [".DS_Store"]
MS_EXTENSION = ".(?:doc|docx|pptx|xlsx|txt)"

# Seperate regex
FILE_NAME = "(^/.+/)*(.+)$"


# Time Format
DATE_FORMAT = "%Y-%m-%d"
DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
