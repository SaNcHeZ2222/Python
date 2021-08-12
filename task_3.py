import os


os.chdir('some_data') #взял файл в материалах урока
list_size = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
dict_file_size = {}
for file in os.listdir():
    for i in range(1, len(list_size)):
        if os.path.getsize(f'/Users/admin/PycharmProjects/pythonlearn/some_data/{file}') > list_size[i-1] and os.path.getsize(f'/Users/admin/PycharmProjects/pythonlearn/some_data/{file}') <= list_size[i]:
            if list_size[i] not in dict_file_size.keys():
                dict_file_size[list_size[i]] = 1
            else: dict_file_size[list_size[i]] += 1
    print(os.path.getsize(f'/Users/admin/PycharmProjects/pythonlearn/some_data/{file}'))
print(dict_file_size)