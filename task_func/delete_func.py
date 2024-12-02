import json

from logic.logic_enter import logic_enter
from logic.logic_file import load_json


def delete_func():
    test = load_json('data/test.json')
    found = False  # flag

    del_i = input('Enter the ID to be deleted: ')
    logic_enter(del_i)

    for i in test:
        if i['id'] == del_i:
            found = True
            test.remove(i)
            break

    if not found:
        print('ID not found')

    with open('data/test.json', 'w') as file:
        json.dump(test, file, indent=4)


if __name__ == '__main__':
    delete_func()
