from src.utils import check_file_or_dir, check_file_format
from src.constants import CheckOutput, FileFormats


def test_check_file_or_dir_file():
    PATH = "./tests/assets/test.json"

    assert check_file_or_dir(PATH) == CheckOutput.FILE


def test_check_file_or_dir_dir():
    PATH = "./tests/assets"

    assert check_file_or_dir(PATH) == CheckOutput.DIR


def test_check_file_or_dir_dne():
    PATH = "./tests/assets/notafile.txt"

    assert check_file_or_dir(PATH) == CheckOutput.DNE


def test_check_file_format_json():
    PATH = "./tests/assets/test.json"

    assert check_file_format(PATH) == FileFormats.JSON


def test_check_file_format_csv():
    PATH = "./tests/assets/test.csv"

    assert check_file_format(PATH) == FileFormats.CSV


def test_check_file_format_other():
    PATH = "./tests/assets/notafile.txt"

    assert check_file_format(PATH) == FileFormats.OTHER
