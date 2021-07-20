list_of_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for index, value in enumerate(list_of_employees):
    print(f'Привет, {value.split()[-1].title()}!')