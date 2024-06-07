import threading

def multi(n):
    for i in range(n):
        print("hello_"+str(i))

multi(5)

