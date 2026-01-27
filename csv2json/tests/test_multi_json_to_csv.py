from src.csv2json import key_discovery, jsons_to_row

HOM_KEY_DATA = [
    {"Key_A": 1, "Key_B": 2, "Key_C": 3},
    {"Key_A": 1, "Key_B": 2, "Key_C": 3},
]
HET_KEY_DATA = [
    {"Key_A": 1, "Key_B": 2, "Key_C": 3},
    {"Key_A": 1, "Key_B": 2, "Key_D": 3},
]


def test_key_discovery_hom_keys():
    disovered_keys, _ = key_discovery(HOM_KEY_DATA)

    assert disovered_keys["Key_A"] == 0
    assert disovered_keys["Key_B"] == 1
    assert disovered_keys["Key_C"] == 2


def test_key_discovery_het_keys():
    disovered_keys, _ = key_discovery(HET_KEY_DATA)

    assert disovered_keys["Key_A"] == 0
    assert disovered_keys["Key_B"] == 1
    assert disovered_keys["Key_C"] == 2
    assert disovered_keys["Key_D"] == 3


def test_jsons_to_rows_hom_data():
    rows = jsons_to_row(HOM_KEY_DATA)

    assert rows[0] == ["Key_A", "Key_B", "Key_C"]
    assert rows[1] == [1, 2, 3]
    assert rows[2] == [1, 2, 3]


def test_jsons_to_rows_het_data():
    rows = jsons_to_row(HET_KEY_DATA)

    assert rows[0] == ["Key_A", "Key_B", "Key_C", "Key_D"]
    assert rows[1] == [1, 2, 3, ""]
    assert rows[2] == [1, 2, "", 3]
