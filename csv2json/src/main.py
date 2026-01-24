from csv2json import load_csv, load_json, csv_to_json, array_json_to_rows


def main() -> None:
    data = load_json("./tests/assets/test_2.json")
    rows = array_json_to_rows(data)

    print(rows)

if __name__ == "__main__":
    main()