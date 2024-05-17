def argstype(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    
    for x, y in kwargs.items():
        print(x, y)


ar =  ['a','b','c']
kar = {'11': 'divya','12': 'Anil'}
argstype(1,*ar,**kar )
    