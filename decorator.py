from logging import info

def logging(func):
    def mfx(*args, **kwargs):
        print(f"calling function {__name__} with args = {args}, kwargs = {kwargs}" )
        result =  func(*args,**kwargs)
        print(f"results from the function {__name__} is {result}")
        #return result
    return mfx


@logging
def add(a,b):
    return a+b

add(2,3)