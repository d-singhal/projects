num=12021
temp=num
rev=0
while(num>0):
    dig=num%10
    print('dig', dig)
    rev=rev*10+dig
    print('rev', rev)
    num=num//10
    print("num" , num)
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")