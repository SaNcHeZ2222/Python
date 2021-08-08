import sys

with open('len_show_sales', 'r', encoding='utf-8') as len_show:
    len_show_sales = int(len_show.readline())
    len_show.close()

with open('bakery.csv', 'r', encoding='utf-8') as read_file:
    len_show = read_file.read().count('\n')
    read_file.close()
# кол-во строчек
try:
    if sys.argv[0] == 'show_sales.py':
        if len(sys.argv) == 1:
            #print(sys.argv)
            with open('bakery.csv', 'r', encoding='utf-8') as read_file:
                print(read_file.read())
                read_file.close()
        elif len(sys.argv) == 2:
            with open('bakery.csv', 'r', encoding='utf-8') as read_file:
                i = 1
                while True:
                    if i >= int(sys.argv[1]):
                        print(read_file.readline(), end='')
                        if i == len_show_sales:
                            break
                    else:
                        read_file.readline()
                    i += 1
                read_file.close()
        elif len(sys.argv) == 3:
            with open('bakery.csv', 'r', encoding='utf-8') as read_file:
                i = 1
                while True:
                    if i >= int(sys.argv[1]) and i <= int(sys.argv[2]):
                        print(read_file.readline(), end='')
                        if i == int(sys.argv[2]):
                            break
                        i+=1
                    else:
                        read_file.readline()
                        i += 1
                print('')
                read_file.close()

except:
    print('Похоже вы что-то написали не так)')