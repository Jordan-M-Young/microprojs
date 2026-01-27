from src.csv2json import csv_to_json, load_csv

TEST_CSV_FILE = "./tests/assets/test.csv"
TEST_NO_HEADERS_CSV_FILE = "./tests/assets/test_no_headers.csv"


def test_csv_to_json_obj_type():
    csv_data = load_csv(TEST_CSV_FILE)

    json_data = csv_to_json(csv_data, has_headers=True)

    assert isinstance(json_data, dict)


def test_csv_to_json_data():
    csv_data = load_csv(TEST_CSV_FILE)

    json_data = csv_to_json(csv_data, has_headers=True)

    assert json_data["Field_A"] == ["1", "4"]
    assert json_data["Field_B"] == ["2", "5"]
    assert json_data["Field_C"] == ["A", "B"]
    assert json_data["Field_D"] == ["1.0", "2.0"]


def test_csv_to_json_no_headers_data():
    csv_data = load_csv(TEST_NO_HEADERS_CSV_FILE)

    json_data = csv_to_json(csv_data, has_headers=False)

    assert json_data["Field_0"] == ["1", "4"]
    assert json_data["Field_1"] == ["2", "5"]
    assert json_data["Field_2"] == ["A", "B"]
    assert json_data["Field_3"] == ["1.0", "2.0"]
