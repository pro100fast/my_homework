def swap_variable(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


print(swap_variable(5, 7))
