import json
import csv


def load_csv(filename: str) -> list:
    with open(filename,'r') as csvf:
        reader = csv.reader(csvf, delimiter=',')
        return [row for row in reader]


def load_json(filename: str) -> dict:
    with open(filename, 'r') as jfile:
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

            #if the last header is null skip it.
            if col_n == first_row_len-1 and not header:
                continue
            
            #initialize an array value for header key or append item to existing array.
            item = data[row_n][col_n]
            if json_data.get(header):
                json_data[header].append(item)
            else:
                json_data[header] = [item]
    
    return json_data


