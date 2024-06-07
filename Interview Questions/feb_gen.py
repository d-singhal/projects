# create febanacci series using generators


def feb(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        c = a+b
        a = b
        b = c

var = feb(100)
print(var.__next__())
print(var.__next__())
print(var.__next__())
print(var.__next__())
print(var.__next__())
print(var.__next__())
print(var.__next__())

# 0,1,1,2,3,5,8


