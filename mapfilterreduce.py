# map is used to map a particular function to all the elements in the sequence and returns a new sequence

list1 = [1,2,4,5,7]
cube =  list(map(lambda a: a*a*a, list1))
print(cube)


# find out the square of even number from the list
def square(a):
    return a*a


lif1 = [3,4,6,7,9,10,22,32,13,15,18,167]
evens = list(filter(lambda a: a%2 == 0, lif1))
print(evens)
square =  tuple(map(square, evens))
print(square)

# reduce will shrink the whole sequence into a since element and is a part of functools module
from functools import reduce
sum =  reduce(lambda a,b : a+b, square)
print(sum)


map()