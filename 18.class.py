# functions

usr=input("Enter the userinput\n")
def p1():
    print ("True")
def p2():
    print ("false")

if (usr == "praveen"):
    p1()
elif (usr == "ajay"):
    p1()
elif (usr == "abhi") or (usr == "kiran"):
    p2()
elif (usr == "dhanjay"):
    p1()
    p2()