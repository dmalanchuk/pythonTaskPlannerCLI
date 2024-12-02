def find_max_id(list):
    return max((test['id'] for test in list), default=0)
