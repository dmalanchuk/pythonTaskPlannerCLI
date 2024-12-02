def logic_enter(x):
    try:
        x = int(x)
    except ValueError:
        print('Please enter an integer')
