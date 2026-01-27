from src.csv2json import array_json_to_rows, load_json


def test_array_json_to_rows_type():
    data = load_json("./tests/assets/test_2.json")
    assert isinstance(array_json_to_rows(data), list)


def test_array_json_to_rows():
    data = load_json("./tests/assets/test_2.json")
    row_data = array_json_to_rows(data)

    assert row_data[0] == ["Field_A", "Field_B", "Field_C"]
    assert row_data[1] == [1, "A", 1.0]
    assert row_data[2] == [2, "B", 2.0]
    assert row_data[3] == [3, "C", 3.0]
