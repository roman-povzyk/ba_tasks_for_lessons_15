def simple_func():
    a = 1
    b = 2
    c = 3
    return a + b + c


print(simple_func.__code__.co_nlocals)
