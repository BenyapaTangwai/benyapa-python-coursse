def f1(a,b):
    print(a*b)
def f1(a,b,c):
    print(a+b-c)
f1(10,20,5)

def add(datatype,*args):
    if datatype == 'int':
        result = 0
    if datatype == 'str':
        result = ''

    for x in args:
        result = result + x
    print(result)

add('int',5,6)
add('str','Srinivas','hello')
add('int',20,30,40,50)