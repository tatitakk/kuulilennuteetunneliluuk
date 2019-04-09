def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False 





print(is_number('10'))


