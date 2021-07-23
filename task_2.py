def num_translate_adv(num):
    if num[0].isupper():
        print(translate_list[num.lower()].title())
    else:
        print(translate_list[num])


translate_list = {
    'one' : 'один',
    'two' : 'два',
    'three' : 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine' : 'девять',
    'ten' : 'десять'
}
num_translate_adv("two")