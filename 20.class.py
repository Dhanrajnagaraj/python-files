## try  and except

try:
    inp1=int(input("Enter the input"))
    if (inp1%2 == 0):
        print ("{0} is even number".format(inp1))
    else:
        print ("{0} is odd number".format(inp1))
except:
    print ("invalid input provided")

======================================================================
##and tell the where and what are the error

try:
    inp1=int(input("Enter the input"))
    if (inp1%2 == 0):
        print ("{0} is even number".format(inp1))
    else:
        print ("{0} is odd number".format(inp1))


except Exception as e:              # "e"  is variable
    print ("invalid input provided and error is {0}".format(e))

=========================================================================    


## after the error user get another chance to enter the input 
try:
    inp1=int(input("Enter the input"))
except Exception as e:
    print ("Input input provided and error is {0} and In next step provide valid input as number".format(e))
    inp1=int(input("Enter the input"))

if (inp1%2 == 0):
    print ("Number {0} is even".format(inp1))
else:
    print ("Number {0} is odd".format(inp1))


==========================================================================

## checking try and except for each input 
def add(a,b):
    ou=n1+n2
    print ("SUM OF {0} and {1} is {2}".format(n1,n2,ou))

def mul(a,b):
    ko=n1*n2
    print ("Product of {0} and {1} is {2}".format(n1,n2,ko))


try:
    n1=int(input("Enter the number1"))
except Exception as e:
    print ("Invalid input provided and error is {0}".format(e))
    n1=int(input("Enter the number input"))

try:
    n2=int(input("Enter the number2"))
except Exception as e:
    print ("Invalid input provided and error is {0}".format(e))
    n2=int(input("Enter the number input"))
try:
    if (type(n1) is int ) and (type(n2) is int):
        usrop=int(input("Enter the Option\n '1' for addition '2' for multiplication"))
        if (usrop == 1):
            add(n1,n2)
        elif (usrop == 2):
            mul(n1,n2)
except:
    print ("Both inputs are not numbers")