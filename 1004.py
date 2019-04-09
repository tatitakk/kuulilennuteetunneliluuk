def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False 



# Oversight


print(is_number('10'))


