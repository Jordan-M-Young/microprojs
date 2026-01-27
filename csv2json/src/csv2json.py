import json
import csv


def load_csv(filename: str) -> list:
    with open(filename, "r") as csvf:
        reader = csv.reader(csvf, delimiter=",")
        return [row for row in reader]


def load_json(filename: str) -> dict:
    with open(filename, "r") as jfile:
        return json.loads(jfile.read())


def csv_to_json(data: list, has_headers=True) -> dict:
    first_row = data[0]
    first_row_len = len(first_row)
    first_row_range = range(first_row_len)
    if has_headers:
        headers = first_row
        data_range = range(len(data))[1:]
    else:
        headers = [f"Field_{i}" for i in first_row_range]
        data_range = range(len(data))

    json_data = {}
    for row_n in data_range:
        for col_n in first_row_range:
            header = headers[col_n]

            # if the last header is null skip it.
            if col_n == first_row_len - 1 and not header:
                continue

            # initialize an array value for header key or append item to existing array.
            item = data[row_n][col_n]
            if json_data.get(header):
                json_data[header].append(item)
            else:
                json_data[header] = [item]

    return json_data


# scenarios


# 1. multiple jsons with same fields
def key_discovery(data: list[dict]) -> dict:
    key_store = {}
    headers = []
    # o(n^2)
    count = 0
    for json in data:
        for key in json.keys():
            if key_store.get(key) is None:
                key_store[key] = count
                count += 1
                headers.append(key)

    return key_store, headers


def jsons_to_row(
    data: list[dict],
) -> list[list]:
    key_map, headers = key_discovery(data)
    n_keys = len(key_map)

    rows = [headers]

    for json in data:
        row = []
        curr_idx = 0
        for key, value in json.items():
            curr_key_idx = key_map[key]

            print(curr_idx, curr_key_idx)

            if curr_idx == curr_key_idx:
                row.append(value)
                curr_idx += 1
                continue

            while curr_idx != curr_key_idx:
                curr_idx += 1
                row.append("")

                if curr_idx == curr_key_idx:
                    row.append(value)
                    curr_idx += 1
                    break

        while curr_idx < n_keys:
            row.append("")
            curr_idx += 1

        rows.append(row)
    return rows


# def mult_json_to_rows(data: list[dict]) -> list:
#     key_store = {}
#     #o(n^2)
#     count = 0
#     for json in data:
#         for key in data.keys():
#             if key_store.get(key):
#                 continue
#             key_store[key] = count
#             count += 1


#     return []


# 2. single json with arrays
def array_json_to_rows(data: dict) -> list:
    max_length = 0
    headers = []
    for key, value in data.items():
        headers.append(key)
        val_length = len(value)
        if val_length > max_length:
            max_length = val_length

    tabular_data = [[] for i in range(max_length)]

    for arr in data.values():
        for idx, value in enumerate(arr):
            tabular_data[idx].append(value)

    tabular_data.insert(0, headers)

    return tabular_data
