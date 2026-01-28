from src.csv2json import load_csv, load_json

TEST_CSV_FILE = "./tests/assets/test.csv"
TEST_JSON_FILE = "./tests/assets/test.json"


def test_load_csv_obj():
    data = load_csv(TEST_CSV_FILE)

    assert isinstance(data, list)


def test_load_csv_data():
    data = load_csv(TEST_CSV_FILE)

    for row in data:
        assert isinstance(row, list)

    assert data[0][0] == "Field_A"
    assert data[1][0] == "1"
    assert data[2][3] == "2.0"


def test_load_json_obj():
    data = load_json(TEST_JSON_FILE)

    assert isinstance(data, dict)


def test_load_json_data():
    data = load_json(TEST_JSON_FILE)
    for key in data.keys():
        assert data[key]

    assert data["field_A"] == 1
    assert data["field_B"] == 2
    assert data["field_C"] == "a"
    assert data["field_D"] == [1, 2, 3]
    assert data["field_E"] == {"sub1": 1, "sub2": "b"}
