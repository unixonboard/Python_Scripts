'''def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner

def num():
    return 5

resultfun = decor(num)

print(resultfun())'''


def decor(fun):
    def inner(c):
        result = fun(c)
        return result*2
    return inner

@decor
def num(n):
    return n

print(num(8))