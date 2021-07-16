ending_withdraw = int(100)
for i in range(1, ending_withdraw+1):
    if i == 1 or (i%10 == 1 and i != 11):
        print(f'{i} процент')
    elif i in [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ,18, 19, 20] or i%10 in [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ,18, 19, 20]:
        print(f'{i} процентов')
    else:
        print(f'{i} процента')