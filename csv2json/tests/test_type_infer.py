from src.type_infer import is_int, is_float


def test_is_int():
    assert is_int("123")
    assert not is_int("1.23")
    assert not is_int("onetwothree")


def test_is_float():
    assert is_float("1.0")
    assert not is_float(".")
