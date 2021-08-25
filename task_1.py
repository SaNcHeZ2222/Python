class Data:

    @classmethod
    def take_data(cls, data):
        [print(int(i), end=' ') for i in data.split('-')]

    @staticmethod
    def check_data(data):
        day = int(data.split('-')[0])
        month = int(data.split('-')[1])
        if day <= 30 and month == (4 or 6 or 9 or 11):
            [print(int(i), end=' ') for i in data.split('-')], print('Такая дата существует')
        elif day <= 31 and month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
            [print(int(i), end=' ') for i in data.split('-')], print('Такая дата существует')
        elif day <=28 and month == 2:
            [print(int(i), end=' ') for i in data.split('-')], print('Такая дата существует')
        else:
            print('Такой даты не существует')




Data.take_data('13-01-2018')
print()
Data.check_data('28-02-2018')


