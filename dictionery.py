dict1 =  {i:f"item_{i}" for i in range(2,10)}
dict2 =  {i:f"item_{i}" for i in range(10)}
print(dict1)
print(dict2)

#print(dict1.keys())
#print(dict1.values())
#print(dict1.items())

for i,j in dict1.items():
    print(i,j)

# "enumarate" function with dictionary to get position index and corresponding index at the same time
for i in enumerate(dict1):
    print(i)

zp =  zip(dict1,dict2)
print(dict(zp))

""" .pop() method :
Pop inside dictionary can be used to remove the last item as well as any specific item.
While in list the pop was just used to remove the last element
ex: dict1.pop("city")"""