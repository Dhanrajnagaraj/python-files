def p1(a=0,b=10):  ##using default value of arguments
    c=a+b
    print ("Sum of {0} and {1} is {2}".format(a,b,c))

p1()

def p1(a=0,b=10):  ##using default value of arguments
    c=a+b
    print ("Sum of {0} and {1} is {2}".format(a,b,c))

n1=int(input("Enter the number1"))
n2=int(input("Enter the number2"))
p1(n1,n2)  ##here we are overriding default values


def p1(a=0,b=10):  ##using default value of arguments
    c=a+b
    print ("Sum of {0} and {1} is {2}".format(a,b,c))

n1=int(input("Enter the number1"))

p1(n1,n2)  ##here we are overriding only a value 