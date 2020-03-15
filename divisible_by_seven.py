def is_divisible(num):
    while num > 0b111:
        last_zero = num & 1 == 0
        num >>= 1

        if not last_zero:
            num += 0b100

    return num == 0b111


print(is_divisible(77))
print(is_divisible(143))
print(is_divisible(21))
print(is_divisible(28))
print(is_divisible(35))
print(is_divisible(15))
