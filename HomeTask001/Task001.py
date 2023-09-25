n = int(input('Введите количество монеток: ',))
k = 0
for i in range(n):
    v = int(input('Введите сторону монетки (0 - Ребро, 1 - Герб): ', ))
    if v == 1:
        k += 1

res = k if k<n/2 else n-k
print('Всего нужно перевернуть монеток', res)
