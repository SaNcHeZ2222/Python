def odd_to(n):
    odd_gen = {i for i in range(1, n+1) if i%2 == 1}
    for i in odd_gen:
        yield i


for i in odd_to(15):
     print(i)