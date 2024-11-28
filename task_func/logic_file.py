from os import path
import json


def load_json(file_name):

    if path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    else:
        return []


if __name__ == '__main__':
    load_json('data/test.json')
