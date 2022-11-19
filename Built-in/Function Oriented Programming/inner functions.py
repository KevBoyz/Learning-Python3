def parent(n):
    def power(n):
        if n > 1:
            return n ** 2
        else:
            return 1
    return power(n)
    
    
print(parent(1))

def funcbox(n):
    def f1():
        return print('f1')
    def f2():
        return print('f2')
    if n == 1:
        return f1
    elif n == 2:
        return f2


f = funcbox(1)
f()