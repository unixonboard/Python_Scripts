def decorfun(n):
    def inner(p):
        result = n(p)
        result += " How are you? "
        return result
    return inner

@decorfun
def hello(name):
    return "Hello "+name

print(hello("Thakur"))