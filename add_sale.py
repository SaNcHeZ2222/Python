import sys


if sys.argv[0] == 'add_sale.py':
    try:
        with open('bakery.csv', 'a', encoding='utf-8') as read_file:
            read_file.write(f'{sys.argv[1]}\n')
            read_file.close()
            with open('len_show_sales', 'r+', encoding='utf-8') as len_show:
                digit = len_show.readline()
                len_show.write(str(int(digit)+1))
                len_show.close()

    except:
        print('Ошибка, похоже вы что-то ввели не так')