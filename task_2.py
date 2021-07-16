def sum_digits_dividing_number():
    sum_dividing_7 = 0
    for j in range(len(list_odd_numbers)):
        a = list(str(list_odd_numbers[j]))
        sum_digits = 0
        for i in range(len(a)):
            sum_digits += int(a[i])
        if sum_digits % 7 == 0:
            sum_dividing_7 += int(list_odd_numbers[j])
    return sum_dividing_7


list_odd_numbers = []
for i in range(1000):
    if i % 2 == 1:
        list_odd_numbers.append(i**3)
print(list_odd_numbers)
print(sum_digits_dividing_number())

for j in range(len(list_odd_numbers)):
    list_odd_numbers[j] += 7

print(sum_digits_dividing_number())