class NotDigit(Exception):
    def __init__(self, txt):
        self.txt = txt

list_digit = []
while True:
    digit = input('Введите число: ')
    if digit == 'stop':
        [print(digit, end=' ')for digit in list_digit]
        break
    try:
        try:
            int(digit)
        except:
            raise NotDigit('Это не число, введите число')
        list_digit.append(int(digit))
    except NotDigit as err:
        print(err)

