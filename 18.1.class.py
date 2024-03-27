def add():
    su=usr1+usr2
    print ("sum of {0} and {1} is {2}".format(usr1,usr2,su))
def sub():
    sub=usr1-usr2
    print("Difference of {0} and {1} is {2}".format(usr1,usr2,sub))

usr1=int(input("Enter the number1\n"))
usr2=int(input("Enter the number2\n"))
if (usr1%2 == 0):
    print ("{0} is even".format(usr1))
    add()
elif (usr1%2 != 0):
    print ("{0} is odd".format(usr1))
    sub()