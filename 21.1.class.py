## for more no of inputs we use *args

def p1(*args):
    for i in args:
        print ("argument value is {0}".format(i))


n1=int(input("Enter the numnber1\n"))
n2=int(input("Enter the number2\n"))
n3=int(input("Enter the number3\n"))
n4=int(input("Enter the number4\n"))
p1(n1,n2,n3,n4)

=============================================================

def p1(*args):
    print ("total no of arguments are passed is {0}".format(args))  ## shows how  many  argsare passed i,e n1,n2,n3,n4
    sum=0
    for i in args:
       sum=sum+i    

    print("sum of all input is {0}".format(sum))


n1=int(input("Enter the numnber1\n"))
n2=int(input("Enter the number2\n"))
n3=int(input("Enter the number3\n"))
n4=int(input("Enter the number4\n"))
p1(n1,n2,n3,n4)

==============================================================