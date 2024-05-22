# create a string such that it does not have a substring with repetative k number of any characters

str1 = "abcccbdddbda"
k = 3


i = 0
print(len(str1))
while i <= len(str1)-k:
    nstr = str1[i:i+k]
    i+=1
    print(nstr)