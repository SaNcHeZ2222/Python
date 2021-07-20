while True:
    result = 0
    sign = ''
    expression = input("Введите выражение в виде (15 * 3): ").split()
    result = int(expression[0])
    if expression[1] == '*':
        result = result * int(expression[2])
    if expression[1] == '**':
        result = result ** int(expression[2])
    if expression[1] == '/':
        result = result / int(expression[2])
    if expression[1] == '//':
        result = result // int(expression[2])
    print(result, type(result))