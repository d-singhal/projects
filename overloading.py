
"""
Method Overloading: 
Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same class shares the same method name having different signatures. Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.
Note: Python does not support method overloading. 
We may overload the methods but can only use the latest defined method."""
def product(a, b):
    p = a * b
    print(p)
 

def product(a, b, c):
    p = a * b*c
    print(p)
 

product(4, 5,7)