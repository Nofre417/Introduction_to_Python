num = int(input('Введите число N: ', ))
m = 1
res = 1

while res < num:
    res = 2 ** m
    m += 1
    if res <= num:
        print(' ', res)