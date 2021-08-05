from itertools import zip_longest

list_people = {}

with open(f'users.csv', 'r', encoding='utf-8') as users_file:
    with open(f'hobby.csv', 'r', encoding='utf-8') as hobby_file:
        if len(users_file.read().split('\n')) < len(hobby_file.read().split('\n')):
            print(1)
        else:
            users_file.close()
            hobby_file.close()
            with open(f'users.csv', 'r', encoding='utf-8') as users_file:
                with open(f'hobby.csv', 'r', encoding='utf-8') as hobby_file:
                    for user, hobby in zip_longest(users_file.read().split('\n'), hobby_file.read().split('\n')):
                        list_people[user] = hobby
                    print(list_people)