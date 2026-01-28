from src.constants import FileFormats, CheckOutput
import os


def check_file_format(filepath: str) -> FileFormats:
    file_format = filepath.split(".")[-1]

    if file_format == "json":
        return FileFormats.JSON
    elif file_format == "csv":
        return FileFormats.CSV
    else:
        return FileFormats.OTHER


def check_file_or_dir(path: str) -> CheckOutput:
    if os.path.isdir(path):
        return CheckOutput.DIR

    if os.path.isfile(path):
        return CheckOutput.FILE

    return CheckOutput.DNE
