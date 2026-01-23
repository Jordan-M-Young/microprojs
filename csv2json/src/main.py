from csv2json import load_csv, load_json, csv_to_json


def main() -> None:
    data = load_csv("./tests/assets/test.csv")
    json_data = csv_to_json(data)

if __name__ == "__main__":
    main()