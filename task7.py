def fact(n):
    count = 0
    result = 1
    while count != n:
        count += 1
        result *= count
        yield result

n = int(input())
for el in fact(n):
    print(el)



