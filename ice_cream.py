def count_ice_cream():
    ice_cream = input('Сколько порций есть:')
    try:
        ice_cream = int(ice_cream)
    except ValueError:
        print('ValueError')

    if ice_cream > 10:
        result = 3 * ice_cream + 8
    else:
        result = ice_cream
    if result in [0, 1, 2, 4, 7]:
        print('No')
    else:
        print('Yes')


count_ice_cream()
