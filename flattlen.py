def f_flattlen(arr):
    for i in arr:
        if type(i) == list:
            f_flattlen(i)
        else:
            lst.append(i)
    return lst


if __name__ == '__main__':
    arr = [1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]]]
    flattlen = [[1, [2, 3, [4, 5], 6, 7], 8, 9, 10]]
    lst = []
    f_flattlen(flattlen)
    print(lst)