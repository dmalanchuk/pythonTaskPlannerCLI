from logic.logic_enter import logic_enter
from logic.logic_file import load_json


def update_func():
    test = load_json('data/test.json')
    upd_id = input('Enter the id of the task: ')
    logic_enter(upd_id)

    for i in test:
        if i['id'] == upd_id:
            pass


