from src.transforms import get_files


def test_get_files():
    PATH = "./tests/assets"

    files = get_files(PATH)

    assert files

    assert files[0] == "./tests/assets/test.csv"
