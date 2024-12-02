import json
from logic.logic_file import load_json
from datetime import datetime


def update_func():
    test = load_json('data/test.json')
    upd_id = input('Enter the id of the task: ')

    task_to_update = next((task for task in test if task['id'] == int(upd_id)), None)

    if not task_to_update:
        print(f"No task found with ID {upd_id}.")
        return

    update_description = input('Enter the new description of the task: ')
    update_status = input('Enter the new status (todo, done, in progress) of the task: ')

    if update_description:
        task_to_update['description'] = update_description
    valid_statuses = ['todo', 'done', 'in progress']

    if update_status:
        if update_status in valid_statuses:
            task_to_update['status'] = update_status
        else:
            print(f"Invalid status. Please choose from {valid_statuses}.")
            return

    task_to_update['updatedAt'] = datetime.now().strftime('%c')

    with open('data/test.json', 'w') as outfile:
        json.dump(test, outfile, indent=4)







