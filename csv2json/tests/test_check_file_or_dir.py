from src.csv2json import check_file_or_dir
from src.constants import CheckOutput


def test_check_file_or_dir_file():
    PATH = "./tests/assets/test.json"

    assert check_file_or_dir(PATH) == CheckOutput.FILE


def test_check_file_or_dir_file():
    PATH = "./tests/assets"

    assert check_file_or_dir(PATH) == CheckOutput.DIR


def test_check_file_or_dir_file():
    PATH = "./tests/assets/notafile.txt"

    assert check_file_or_dir(PATH) == CheckOutput.DNE
