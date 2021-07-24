def thesaurus_adv(*args):
    dict_full_name = {}
    for i in range(len(args)):
        first_letter_surname = args[i].split()[1][0]
        first_letter_name = args[i].split()[0][0]
        if first_letter_surname not in dict_full_name.keys():
            dict_full_name[first_letter_surname] = {}
            if first_letter_name not in dict_full_name[first_letter_surname].keys():
                dict_full_name[first_letter_surname][first_letter_name] = [args[i]]
            else:
                dict_full_name[first_letter_surname][first_letter_name].append(args[i])
        else:
            if first_letter_name not in dict_full_name[first_letter_surname].keys():
                dict_full_name[first_letter_surname][first_letter_name] = [args[i]]
            else:
                dict_full_name[first_letter_surname][first_letter_name].append(args[i])
    print(dict_full_name)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Вася Алексеев", "Илья Иванов", "Анна Савельева", "Марина Андреевна", "Алла Ильинична")