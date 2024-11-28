from task_func.add_func import add_func
from task_func.delete_func import delete_func

"""
    Вимоги:
    Додаток повинен працювати з командного рядка, приймати дії користувача та вхідні дані як аргументи 
    та зберігати завдання у файлі JSON. Користувач повинен мати можливість:
    
    Завдання додавання, оновлення та видалення
    Позначити завдання як виконане або виконане
    Перерахуйте всі завдання
    Перерахуйте всі виконані завдання
    Перерахуйте всі завдання, які не виконані
    Перерахуйте всі завдання, які виконуються
    
    Властивості завдання:
    Кожне завдання має мати такі властивості:
    
    id: Унікальний ідентифікатор для завдання
    description: Короткий опис завдання
    status: Статус завдання (todo, in-progress, done)
    createdAt: Дата та час створення завдання
    updatedAt: Дата та час останнього оновлення завдання
"""


if __name__ == '__main__':
    inp = input('choose action: ')
    while inp != 'exit':
        if inp == 'add' or inp == 'a':
            add_func()
            break
        elif inp == 'delete' or inp == 'd':
            delete_func()
            break
        elif inp == 'update' or inp == 'u':
            pass
        elif inp == 'task list' or inp == 'tl':
            pass
        elif inp == 'task done' or inp == 'td':
            pass
        elif inp == 'task not done' or inp == 'tnd':
            pass
        elif inp == 'task progress' or inp == 'tp':
            pass
        else:
            print('invalid input')
            break
