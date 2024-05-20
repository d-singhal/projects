def generator(n):
    for i in range(n):
        yield i
gener =  generator(1000000)
print(gener)
print(next(gener))
print(next(gener))

#another way to call all the yielded values
gen =  generator(50)
for j in gen:
    print(j)