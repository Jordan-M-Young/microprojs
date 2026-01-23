from csv2json import load_csv, load_json


def main() -> None:
    data = load_csv("./tests/assets/test.csv")
    print(data[0][0])

if __name__ == "__main__":
    main()