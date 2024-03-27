a1={'a':'10'}
b1={'g':'20'}

if (type(a1) is list)  and (type(b1) is list):
    c=a1+b1
    print (c)
elif (type(a1) is dict) and (type(b1) is dict):
    b1.update(a1)
    print (b1)