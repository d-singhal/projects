# create febanacci series using generators

def feb(n):
    for i in range(0,n):
        a = 0
        b = 1
        c = a+b
        b = a+b
        yield a+b

var = feb(5)
print(var.__next__())
print(var.__next__())
print(var.__next__())
print(var.__next__())

# 0,1,1,2,3,5,8
