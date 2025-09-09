from multipledispatch import dispatch
@dispatch(int,int)
def product(a,b):
    result = a * b
    print(result)

@dispatch(int,int,int)
def product(a,b,c):
    result = a * b * c
    print(result)

@dispatch(str,str)
def product(a,b):
    restlt = a +' '+ b
    print(restlt)

product(10,20)
product(10,20,10)
product('Hello','Rumi')