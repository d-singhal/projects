def argstype(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    
    for x, y in kwargs.items():
        print(x, y)

# args take tuple **kwargs take dict
ar =  ['a','b','c']
kar = {'11': 'divya','12': 'Anil'}
argstype(1,*ar,**kar )
    