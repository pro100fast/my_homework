"""
def search_extra(num):
    for i in range(0, len(num)):
        for j in range(i + 1, len(num)):
            if num[i] ^ num[j] == 0:
                num[i] = 0
                num[j] = 0
    for elem in num:
        if elem != 0:
            return elem
    return elem


arr = [2, 6, 2, 6, 1, 1, 5, 5, 7, 7, 15, 15, 3, 15, 15, 5]
counter = [i for i in arr]
print(arr, search_extra(counter))
"""


def one_extra(arr):
    i = 0
    for el in arr:
        i ^= el
    return i


if __name__ == '__main__':
    print(one_extra([1, 2, 4, 1, 15, 15,  4, 5, 2]))
