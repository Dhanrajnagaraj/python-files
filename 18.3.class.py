def even():
    print ("Number {0} is even".format(usr))
    usrop=int(input("Enter '1' to perform addition\n'2' for diffe"))
    if (usrop == 1):
        suk=usr+usr2
        print ("Sum of {0} and {1} is {2}".format(usr,usr2,suk))
    elif (usrop == 2):
        subk=usr-usr2
        print ("Difference of {0} and {1} is {2}".format(usr,usr2,subk))

def odd():
    print ("Number {0} is odd".format(usr))
    usrop=int(input("Enter '1' to perform mult\n'2' for div"))
    if (usrop == 1):
        suk=usr*usr2
        print ("product of {0} and {1} is {2}".format(usr,usr2,suk))
    elif (usrop == 2):
        subk=usr/usr2
        print ("division of {0} and {1} is {2}".format(usr,usr2,subk))


usr=int(input("Enter the userinput\n"))
usr2=int(input("Enter the userinput\n"))
if (usr%2 == 0):
    even()
elif (usr%2 != 0):
    odd()