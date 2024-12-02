from logic.logic_file import load_json


def valid_status(x: str):
    test = load_json('data/test.json')
    r = [t for t in test if t['status'] == x]
    if r:
        for task in r:
            print(f'id: {task['id']}, description: {task['description']}, status: {task['status']}')
    else:
        print(f'No tasks with status "{x}"')


def task_func():
    test = load_json('data/test.json')

    task_list = input('1. list \n2. todo \n3. done \n4. in progress \nEnter the task list: ')

    if task_list == '1' or task_list.lower() == 'list':
        for l in test:
            print(f'id: {l['id']}, description: {l['description']}, status: {l['status']}')
    elif task_list == '2' or task_list.lower() == 'todo':
        valid_status('todo')
    elif task_list == '3' or task_list.lower() == 'done':
        valid_status('done')
    elif task_list == '4' or task_list.lower() == 'in progress':
        valid_status('in progress')
    else:
        print('Invalid input')

