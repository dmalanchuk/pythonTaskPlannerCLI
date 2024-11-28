import json
from task_func.logic_file import load_json
from time import asctime


def add_func():
    file_name = 'data/test.json'
    date_now = asctime()
    last_upd = asctime()
    test = load_json(file_name)

    description = input('add new task: ')
    max_id = max((test['id'] for test in test), default=0)

    new_tasks = {
        'id': max_id + 1,
        'description': f'{description}',
        'status': 'todo',
        'createdAt': f'{date_now}',
        'updatedAt': f'{last_upd}',
    }

    test.append(new_tasks)

    with open(file_name, 'w') as file:
        json.dump(test, file, indent=4)


if __name__ == '__main__':
    add_func()
