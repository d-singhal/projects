ls = [i for i in range(10) if i%3 == 0]
print(ls)


# dict comprehension
dc = {
    i:f"item_{i}" for i in range(100) if i%5 == 0
}

dc1 =  {value:key for key,value in dc.items()}
dc2 =  {i:i*2 for i in range(5)}
print(dc2)
#print(dc1)


# set comprehension
st = {a for a in ['s','b', 'a', 's']}
#print(st)


# generator comprehension
# using () as syntax

gen_even =  (i for i in ls if i%2 == 0)
print(gen_even.__next__())
print(next(gen_even))
"""for j in gen_even:
    print(j)"""
