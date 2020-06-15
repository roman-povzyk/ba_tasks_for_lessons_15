def minus_ten(x):
    return x - 10


def mult_four(f):
    def resulting_func(x):
       return f(x) * 4
    return resulting_func


result = mult_four(minus_ten)
print(result(15))