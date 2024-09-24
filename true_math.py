# This is a function number 2 dived by zero from module_4_1

def divide(first, second):
    from math import inf
    return first / second if second != 0 else inf
