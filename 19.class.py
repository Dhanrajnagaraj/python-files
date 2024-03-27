def add():
    co=i+usrinput
    print ("Sum of {0} and {1} is {2}".format(i,usrinput,co))
def sub():
    co=i-usrinput
    print ("Difference of {0} and {1} is {2}".format(i,usrinput,co))

def prod():
    co=i*usrinput
    print ("Product of {0} and {1} is {2}".format(i,usrinput,co))
def divis():
    co=i/usrinput
    print ("Division of {0} and {1} is {2}".format(i,usrinput,co))

usrinput=int(input("Enter the number\n"))
for i in range(0,101,1):
    if (i > 0) and (i<40):
        add()
    elif (i>40) and (i<60):
        sub()
    elif (i>60) and (i<80):
        prod()
    elif (i == 98):
        add()
        sub()
        prod()
        divis()
    else:
        divis()
    print ("===================================================================")

