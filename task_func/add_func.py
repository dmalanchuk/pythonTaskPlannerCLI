import json
from time import asctime
from os import path


def add_func():
    date_now = asctime()
    last_upd = asctime()

    file_name = 'data/test.json'

    if path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                test = json.load(file)
            except json.JSONDecodeError:
                test = []
    else:
        test = []

    max_id = max((test['id'] for test in test))
    description = input('add new task: ')

    new_task = {
        'id': max_id + 1,
        'description': f'{description}',
        'status': 'todo',
        'createdAt': f'{date_now}',
        'updatedAt': f'{last_upd}',
        }

    test.append(new_task)

    with open(file_name, 'w') as file:
        json.dump(test, file, indent=4)


if __name__ == '__main__':
    add_func()
