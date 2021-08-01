from itertools import zip_longest

tutors = ['Иван', "Анастасия", "Петр", "Сергей", "Дмитрий", "Борис", "Елена", "Вася", "Петя"]
klasses = ["9А", "7В", "9Б", "8Б", "10А", "10Б", "9А"]

dasd = ((tutor, klass) if len(tutors)>len(klasses) and i<len(klasses) else (tutor, None) for tutor, klass, i in zip_longest(tutors, klasses, range(len(tutors))))
print(dasd)
for i in dasd:
    print(i)