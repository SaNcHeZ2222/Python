def thesaurus(*args):
    dict_name = {}
    for i in range(len(args)):
        if args[i][0] in dict_name.keys():
            dict_name[args[i][0]].append(args[i])
        else:
            dict_name.setdefault(f'{args[i][0]}', [f'{args[i]}'])
    print(dict_name)


thesaurus("Иван", "Мария", "Петр", "Илья", 'Сашка', 'Марина', 'Ирина')