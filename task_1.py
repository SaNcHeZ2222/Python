import re

RE_NAME = re.compile(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)")


input_mail = 'soMeone@geekbrains.ru'
dict_mail = {}

if re.findall(RE_NAME, input_mail):
    dict_mail['username'] = input_mail.split('@')[0]
    dict_mail['domain'] = input_mail.split('@')[1]
    print(dict_mail)
else:
    print(f'ValueError: wrong email: {input_mail}')