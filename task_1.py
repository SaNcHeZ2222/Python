while True:
    duration = int(input('Введите время(сек): '))
    minute = duration // 60
    hour = duration // (3600)
    day = duration // (3600 * 24)
    if duration > 60 and duration <= 3600:
        print(f'{minute} мин {duration%60} сек')
    elif duration > 3600 and duration <= 3600*24:
        print(f'{hour} час {abs((3600*hour-duration))//60} мин {duration%60} сек')
    elif duration > 3600*24 and duration <= 3600*24*30:
        print(f'{day} дн {abs((86400*day-duration)//3600)-1} час {abs((3600*hour-duration))//60} мин {duration%60} сек')
    elif duration > 3600*24*30:
        print(f'Дальше не делал, только до месяца')
    else:
        print(f'{duration} сек')

