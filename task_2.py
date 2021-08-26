class DelNull(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    try:
        expression = (13 / 1)
        print(expression)
    except:
        raise DelNull('Нельзя делить на ноль')
except DelNull as err:
    print(err)

