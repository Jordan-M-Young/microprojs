from enum import Enum

JSON2CSV = "json2csv"
CSV2JSON = "csv2json"


class CheckOutput(Enum):
    FILE = "file"
    DIR = "dir"
    DNE = "dne"


class FileFormats(Enum):
    CSV = "csv"
    JSON = "json"
    OTHER = "other"
