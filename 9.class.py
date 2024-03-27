# n1=int(input("Enter the number1\n"))
# n2=int(input("Enter the number2\n"))
# print ("Enter '1' for addition\n'2' for subtraction\n'3' for Multiplication\n'4' for division\n'5' for adtion subtraction multiplication")
# usrinpu=input("Enter the User option\n")
# if (usrinpu == "1"):
#     su=n1+n2
#     print ("Sum of number {0} and {1} is {2}".format(n1,n2,su))
# elif (usrinpu == "2"):
#     sub=n1-n2
#     print ("Diference of {0} and {1} is {2}".format(n1,n2,sub))
# elif (usrinpu == "3"):
#     mult=n1*n2
#     print ("Product of {0} and {1} is {2}".format(n1,n2,mult))
# elif (usrinpu == "4"):
#     divs=n1/n2
#     print ("Division of {0} and {1} is {2}".format(n1,n2,divs))
# elif (usrinpu == "5"):
#     su=n1+n2
#     sub=n1-n2
#     mult=n1*n2
#     divs=n1/n2
#     print("Sum of number {0} and {1} is {2}".format(n1, n2, su))
#     print("Diference of {0} and {1} is {2}".format(n1, n2, sub))
#     print("Product of {0} and {1} is {2}".format(n1, n2, mult))
#     print("Division of {0} and {1} is {2}".format(n1, n2, divs))


'''
usrinp=input("Enter the input\n")
print (dir(usrinp))
if (usrinp.isalpha()):
    print ("User input is alphabet and user input is {0}".format(usrinp))
    letter_check=input("Enter the character to be checked")

    if (letter_check in usrinp):
        print ("{1} present in user input {0}".format(usrinp,letter_check))
        print ("_".join(usrinp))
    else:
        print ("{1} not present in user input {0}\nNow we will 'a' to user input ".format(usrinp,letter_check))
        add_a=usrinp+letter_check
        print (add_a)
        print ("New value post adding {2} to {0} and final output is {1}".format(usrinp,add_a,letter_check))
elif (usrinp.isdigit()):
    print ("Userinput {0} is number".format(usrinp))
elif (usrinp.isalnum()):
    print ("Userinput {0} contains both alphabet and number".format(usrinp))
'''


'''
usrinp = input("Enter the input\n")
print(dir(usrinp))

if (usrinp.isalpha()):
    print("User input is alphabet and user input is {0}".format(usrinp))
    letter_check = input("Enter the character to be checked")

    if (letter_check in usrinp):
        print("{1} present in user input {0}".format(usrinp, letter_check))
        print("_".join(usrinp))
    else:
        print("{1} not present in user input {0}\nNow we will 'a' to user input ".format(usrinp, letter_check))
        add_a = usrinp + letter_check
        print(add_a)
        print("New value post adding {2} to {0} and final output is {1}".format(usrinp, add_a, letter_check))
elif (usrinp.isdigit()):
    print("Userinput {0} is number".format(usrinp))
    print(dir(usrinp))
    print(type(usrinp))

    if (usrinp is int):
        n2 = int(input("Enter the Number\n"))
        su = usrinp + n2
        print("User input {0} already is integer and added {1} sum is {2}".format(usrinp, n2, su))
    else:
        print("user input {0} is not integer\nNow we are converting to integer".format(usrinp))
        con_us = int(usrinp)
        print(type(con_us))
        print("Now converted input is {0} and its type is {1}".format(con_us, type(con_us)))

elif (usrinp.isalnum()):
    print("Userinput {0} contains both alphabet and number".format(usrinp))
    
'''

'''
n1=int(input("Enter the number1\n"))
n2=int(input("Enter the number2\n"))
print ("Enter '1' for addition\n'2' for subtraction\n'3' for Multiplication\n'4' for division\n'5' for adtion subtraction multiplication")
usrinpu=input("Enter the User option\n")
if (usrinpu == "1"):
    su=n1+n2
    print ("Sum of number {0} and {1} is {2}".format(n1,n2,su))
elif (usrinpu == "2"):
    sub=n1-n2
    print ("Diference of {0} and {1} is {2}".format(n1,n2,sub))
elif (usrinpu == "3"):
    mult=n1*n2
    print ("Product of {0} and {1} is {2}".format(n1,n2,mult))
elif (usrinpu == "4"):
    divs=n1/n2
    print ("Division of {0} and {1} is {2}".format(n1,n2,divs))
elif (usrinpu == "5"):
    out=[]
    su=n1+n2
    sub=n1-n2
    mult=n1*n2
    divs=n1/n2
    print("Sum of number {0} and {1} is {2}".format(n1, n2, su))
    print("Diference of {0} and {1} is {2}".format(n1, n2, sub))
    print("Product of {0} and {1} is {2}".format(n1, n2, mult))
    print("Division of {0} and {1} is {2}".format(n1, n2, divs))
    out.append(su)
    out.append(sub)
    out.append(mult)
    out.append(divs)
    print (out)

'''

'''
n1=int(input("Enter the number1\n"))
n2=int(input("Enter the number2\n"))
print ("Enter '1' for addition\n'2' for subtraction\n'3' for Multiplication\n'4' for division\n'5' for adtion subtraction multiplication")
usrinpu=input("Enter the User option\n")
if (usrinpu == "1"):
    su=n1+n2
    print ("Sum of number {0} and {1} is {2}".format(n1,n2,su))
elif (usrinpu == "2"):
    sub=n1-n2
    print ("Diference of {0} and {1} is {2}".format(n1,n2,sub))
elif (usrinpu == "3"):
    mult=n1*n2
    print ("Product of {0} and {1} is {2}".format(n1,n2,mult))
elif (usrinpu == "4"):
    divs=n1/n2
    print ("Division of {0} and {1} is {2}".format(n1,n2,divs))
elif (usrinpu == "5"):
    out=[]
    dictot={}
    su=n1+n2
    sub=n1-n2
    mult=n1*n2
    divs=n1/n2
    print("Sum of number {0} and {1} is {2}".format(n1, n2, su))
    print("Diference of {0} and {1} is {2}".format(n1, n2, sub))
    print("Product of {0} and {1} is {2}".format(n1, n2, mult))
    print("Division of {0} and {1} is {2}".format(n1, n2, divs))
    out.append(su)
    out.append(sub)
    out.append(mult)
    out.append(divs)
    dictot['add']=su
    dictot['sub']=sub
    dictot['mult']=mult
    dictot['divisi']=divs
    print (out)
    print (dictot)

'''

'''
userinp=input("Enter the input\n")
if (userinp.isalpha()):
    print ("Userinput {0} is alphabet".format(userinp))
    if (userinp.isupper()):
        conv_lowe=userinp.lower()
        print ("Orginal input {0}  and we converted to lowercase is {1}".format(userinp,conv_lowe))
    elif(userinp.islower()):
        con_upper=userinp.upper()
        print ("Orginal input {0} and we converted to uppercase is {1}".format(userinp,con_upper))
else:
    print ("Input {0} is not alphabet".format(userinp))
    
'''

userinp=input("Enter the input\n")
if (userinp.isalpha()):
    print ("Enter '1' to check convert to lower\n'2' to check an convert upper case\n'3' to swapcase")
    userop=input("Enter the useropt\n")
    if (userop == "1"):
        if (userinp.islower()):
            print ("Userinput {0} already in lowercase".format(userinp))
        else:
            print ("user input {0} not in lowecase".format(userinp))
            usrcon=input("Enter 'yes' to conver lowercase")
            if (usrcon == "yes"):
                print ("User confirmed to convert {0} to lwoer case".format(userinp))
                conve_low=userinp.lower()
                if (conve_low.islower()):
                    print ("Orginal string {0} is successfully convert to lower case {1}".format(userinp,conve_low))

            else:
                print ("User not confirmed to convert {0} to lowercase".format(userinp))
    elif (userop == "2"):
        if (userinp.isupper()):
            print("Userinput {0} already in uppercase".format(userinp))
        else:
            print("user input {0} not in uppercase".format(userinp))
            usrcon = input("Enter 'yes' to conver uppercase")
            if (usrcon == "yes"):
                print("User confirmed to convert {0} to upper case".format(userinp))
                conve_low = userinp.upper()
                if (conve_low.isupper()):
                    print("Orginal string {0} is successfully convert to upper case {1}".format(userinp, conve_low))

            else:
                print("User not confirmed to convert {0} to uppercase".format(userinp))
    elif (userop == "3"):
        print ("Orginal string is {0} and now we swapping the case".format(userinp))
        swa_case=userinp.swapcase()
        print ("Swaaped vcase is {0}".format(swa_case))
