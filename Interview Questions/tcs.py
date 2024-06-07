"""tup = (1,[4,2,2],2)
for i in tup:
    if isinstance(i,list):
        i.append(10)
print(type(tup))
"""
"""l1 = [1,2,3,4]
l2 = [3,4,5,6]
find the common from l1 and l2 without using loop or inbuilt function
"""
#dict = {1:2,3:4,5:6}
"""l11 = [1,2,3,4,5,6,7,8,9,10]
{3:9,4:64}
create dic: {odd:odd**2, even:even**3}
create duct2 = {1:2, 3:4, odd:even} --- list of odd keys and even values form l1
dic = {key:key**2 for key in l11 if key%2 != 0}
print(dic)

str =  'abcdefgh'  # reverse the second half of the string only"""

"""x = 123
add1 = 0
def add(x):
    i =  x%10
    rem = x//10
    print(add1+i)
    add(rem)

add(123)"""
    

        





"""l11 = [1,2,3,4,5,6,7,8,9,10]
dict = {k:(k**2 if k%2 == 0 else k**3) for k in l11}
print(dict)
d = (k for k in l11 if k%2 == 0)
d1 = (j for j in l11 if j%2 !=0)
d2 = {zip(d,d1)}
print(dict(d2))"""
    


print ("==================================================================================")
str =  'abcdefgh'
final = str[:len(list(str))//2] +(str[len(list(str))//2:])[::-1]
#print(final)



import re

name = "my 'name, is,divya@ singhal.1"
parts = re.split(r'(\s|,|\.)', name)
print(parts)
reversed_parts = [part[::-1] if part.isalnum() else part for part in parts]
output = ''.join(reversed_parts)

print(output)




