# Main focus to keep pushing the Largest element at the end of the array

a = [12,11,21,1,5,3,7]
for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            continue
    i+=1
    j+=1    
    print(a)