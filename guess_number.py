import random
import time

count = 0

while True:
    random_number = random.randint(1, 10)
    enter_number = input('Введите значение от 1 до 10:')

    count += 1
    print('Число пользователя', enter_number)
    print('Рандомное число :', random_number)

    if int(enter_number) > int(random_number):
        print('Число пользователя больше')
    elif int(enter_number) < int(random_number):
        print('Число пользователя меньше')
    elif int(enter_number) == int(random_number):
        print('Поздравляю, вы угадали число', random_number)
        print('Количество попыток :', count)
        break

time.sleep(60)
