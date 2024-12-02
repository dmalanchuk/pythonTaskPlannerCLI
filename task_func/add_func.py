import json
from datetime import datetime

from logic.finding_max_id import find_max_id
from logic.logic_file import load_json


def add_func():
    date_now = datetime.now().strftime('%c')
    last_upd = datetime.now().strftime('%c')
    test = load_json('data/test.json')

    description = input('add new task: ')
    max_id = find_max_id(test)

    new_tasks = {
        'id': max_id + 1,
        'description': f'{description}',
        'status': 'todo',
        'createdAt': f'{date_now}',
        'updatedAt': f'{last_upd}',
    }

    test.append(new_tasks)

    with open('data/test.json', 'w') as file:
        json.dump(test, file, indent=4)


if __name__ == '__main__':
    add_func()
