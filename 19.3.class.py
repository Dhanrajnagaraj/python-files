##passing arguments in functions

def k(a,b):
    v=a*b
    print(v)

k(3,4)

=========================================

def alaphabet(inp1,inp2):
    print ("Both inputs are alphabet")
    ko=inp1+inp2
    print ("Combining {0} and {1} is {2} and length of character is {3}".format(inp1,inp2,ko,len(ko)) )

def num(inp1,inp2):
    print ("Both inputs are number")
    usrop=int(input("Enter '1' for addition\n'2' for subtraction\n'3' for multiplication"))
    if (usrop == 1):
        sumo=int(inp1)+int(inp2)
        print ("Sum of {0} and {1} is {2}".format(inp1,inp2,sumo))
    elif (usrop == 2):
        sumo=int(inp1)-int(inp2)
        print ("differenc of {0} and {1} is {2}".format(inp1,inp2,sumo))
    elif (usrop == 3):
        sumo=int(inp1)*int(inp2)
        print ("product  of {0} and {1} is {2}".format(inp1,inp2,sumo))

def alphabet_number(inp1,inp2):
    print ("Input are different datatypes")
    nkl=str(inp1)+str(inp2)
    print ("Combining {0} and {1} is {2}".format(inp1,inp2,nkl))

inp1=input("Enter the input1\n")
inp2=input("Enter the input2\n")

if (inp1.isalpha()) and (inp2.isalpha()):
    alaphabet(inp1,inp2)
elif (inp1.isdigit()) and (inp2.isdigit()):
    num(inp1,inp2)
elif (inp1.isdigit()) and (inp2.isalpha()):
    alphabet_number(inp1,inp2)