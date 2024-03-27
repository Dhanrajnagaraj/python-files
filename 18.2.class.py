def add():
    su=usr1+usr2
    print ("sum of {0} and {1} is {2}".format(usr1,usr2,su))
def sub():
    sub=usr1-usr2
    print("Difference of {0} and {1} is {2}".format(usr1,usr2,sub))

usr1=int(input("Enter the number1\n"))
usr2=int(input("Enter the number2\n"))
div1=int(input("Enter the divisor1\n"))
div2=int(input("Enter the divisor2\n"))
if (usr1%2 == 0):
    print ("{0} is even".format(usr1))
    add()
elif (usr1 ==  5):
    add()
    sub()

elif (usr1%2 != 0):
    print ("{0} is odd".format(usr1))
    sub()
    if (usr1%div1 == 0) and (usr1%div2 == 0):
        print ("{0} is divisable by {1} and {2}".format(usr1,div1,div2))
    elif (usr1%div1 == 0):
        print ("{0} is divsable by {1}".format(usr1,div1))
    elif (usr1%div2 == 0):
        print ("{0} is divisable by {2}".format(usr1,div2))
    elif (usr1%div1 != 0) and (usr1%div2 !=0):
        print ("{0} is not divisable by {1} and {2}".format(usr1,div1,div2))


===================================OR=====================================================


def add():
    su=usr1+usr2
    print ("sum of {0} and {1} is {2}".format(usr1,usr2,su))
def sub():
    sub=usr1-usr2
    print("Difference of {0} and {1} is {2}".format(usr1,usr2,sub))

def complediv_both():
        print ("{0} is divisable by {1} and {2}".format(usr1,div1,div2))
        com_usr=int(input("Enter anothet input\n"))
        pro=(usr1+usr2)*com_usr
        print ("sum of {0} and {1} and multipled by {2} and output is {3}".format(usr1,usr2,com_usr,pro))
def divisable_first():
    print("{0} is divsable by {1}".format(usr1, div1))
def divisable_second():
    print ("{0} is divisbale by {2}".format(usr1,div2))
def notdivisable():
    print ("{0} not divsable by {1} and {2}".format(usr1,div1,div2))

usr1=int(input("Enter the number1\n"))
usr2=int(input("Enter the number2\n"))
div1=int(input("Enter the divisor1\n"))
div2=int(input("Enter the divisor2\n"))
if (usr1%2 == 0):
    print ("{0} is even".format(usr1))
    add()
elif (usr1 ==  5):
    add()
    sub()

elif (usr1%2 != 0):
    print ("{0} is odd".format(usr1))
    sub()
    if (usr1%div1 == 0) and (usr1%div2 == 0):
        complediv_both()
    elif (usr1%div1 == 0):
        divisable_first()
    elif (usr1%div2 == 0):
        divisable_second()
    elif (usr1%div1 != 0) and (usr1%div2 !=0):
        notdivisable()