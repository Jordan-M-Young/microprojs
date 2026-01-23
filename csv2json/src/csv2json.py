import json
import csv


def load_csv(filename: str) -> list:
    with open(filename,'r') as csvf:
        reader = csv.reader(csvf, delimiter=',')
        return [row for row in reader]


def load_json(filename: str) -> dict:
    with open(filename, 'r') as jfile:
        return json.loads(jfile.read())



