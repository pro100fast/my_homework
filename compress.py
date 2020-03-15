compress = list([4, 0, 5, 0, 3, 0, 0, 5])
print(compress)


def func(mass):
    start = 0
    for i, el in enumerate(mass):
        if el:
            mass[start], mass[i] = mass[i], mass[start]
            start += 1
    return mass


new_arr = (func(compress))
print(new_arr)