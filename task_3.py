my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(my_list)):
    try:
        if int(my_list[i]) % 10 == int(my_list[i]):
            my_list[i] = '"' + my_list[i][:-1] + '0' + my_list[i][-1:] + '"'
        elif int(my_list[i]) == int(my_list[i]):
            my_list[i] = '"' + my_list[i] + '"'
    except:
        continue

for index, value in enumerate(my_list):
    print(value, end=' ')