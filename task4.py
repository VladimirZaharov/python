def my_func(x,y):
    answer = 1/(x**abs(y))
    return answer

def another_func(x,y):
    z = x*x
    for i in range(2, abs(y)):
        z = z*x
    answer = 1/z
    return answer
