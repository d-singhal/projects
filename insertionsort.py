"""
insertion sort in which the 
Total passes =  n-1
total comparisions  =  1+2+3+4 ---- n-1 =  n(n-1)/2  == O(n**2)
best case = O(n)
stable algorithm as the position of same elements wont move 
adaptive ==> if the array is alreayd sorted it is able to take advantage hence adaptive
"""

a = [12,11,21,1,32,11,24,14]
def sort(a):
    for i in range(1,len(a)):
        temp =  a[i]
        for j in range(i, 0, -1):
            if a[j-1] > temp:
                a[j-1] ,a[j] = a[j], a[j-1]
        i+=1
    return a

print(sort(a))
    