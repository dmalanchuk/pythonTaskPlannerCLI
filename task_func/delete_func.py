import json
from task_func.logic_file import load_json


def delete_func():
    file_name = 'data/test.json'
    test = load_json(file_name)

    del_i = input('Enter the ID to be deleted: ')

    for i in test:
        if i['id'] == int(del_i):
            break
        else:
            print('There is no such task')
            break


if __name__ == '__main__':
    delete_func()
