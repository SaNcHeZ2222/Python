prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

print(id(prices))

for i in range(len(prices)):
    if str(prices[i]).count('.'):
        rub = str(prices[i]).split('.')[0]
        kop = str(prices[i]).split('.')[1]
        if kop.count('0') == 1:
            kop = kop[1:]
        elif len(kop) == 1:
            kop = kop + '0'
        print(f"{rub} руб {kop} коп,", end=' ')
    else:
        print(f'{prices[i]} руб,', end=' ')

print()
print(id(prices))

for i in range(len(prices)):
    if str(prices[i]).count('.'):
        rub = str(prices[i]).split('.')[0]
        kop = str(prices[i]).split('.')[1]
        if kop.count('0') == 1:
            kop = kop[1:]
        elif len(kop) == 1:
            kop = kop + '0'
        prices[i] = (f"{rub} руб {kop} коп,")
    else:
        prices[i] = (f'{prices[i]} руб,')

prices.sort()
for index, value in enumerate(prices):
    print(value, end=' ')

print()
print(id(prices))

new_prices_list = sorted(prices, reverse=True)
for i in range(1, 6):
    print(new_prices_list[i], end=' ')

print()
print(id(new_prices_list))
