'''
usrinp=input("Enter the number\n")
if (int(usrinp)%2 == 0 ):
    print ("{0} is even".format(usrinp))
    c=input("Enter the another input\n")
    print ("Enter '1' for addition\n'2' for multiplciation\n")
    usropt=input("Enter user option\n")
    if (usropt == "1"):
        su=int(usrinp)+int(c)
        print ("Sum of {0} and {1} is {2}".format(usrinp,c,su))
    elif (usropt == "2"):
        mu=int(usrinp)*int(c)
        print ("Product of {0} and {1} is {2}".format(usrinp,c,mu))

else:
    print ("{0} is odd".format(usrinp))
    if (int(usrinp) == 15):
        ano=int(input("Enter the another input\n"))
        sul=int(usrinp)+ano
        print ("User input is {0} and added {1} and sum is {2}".format(usrinp,ano,sul))
    elif (int(usrinp)%3 == 0):
        print ("{0} is odd and its completely divisible by 3".format(usrinp))
    else:
        print ("{0} is odd and its not 15 and its not completely divisible by 3".format(usrinp))


usrinp=input("Enter the number\n")
if (int(usrinp)%2 == 0 ):
    print ("{0} is even".format(usrinp))
    c=input("Enter the another input\n")
    print ("Enter '1' for addition\n'2' for multiplciation\n")
    usropt=input("Enter user option\n")
    if (usropt == "1"):
        su=int(usrinp)+int(c)
        print ("Sum of {0} and {1} is {2}".format(usrinp,c,su))
    elif (usropt == "2"):
        mu=int(usrinp)*int(c)
        print ("Product of {0} and {1} is {2}".format(usrinp,c,mu))

else:
    print ("{0} is odd".format(usrinp))
    divs1=int(input("Enter the divisor1"))
    divs2=int(input("Enter the divisor2"))
    if (int(usrinp)%divs1 == 0) and (int(usrinp)%divs2 == 0):
        print ("{0} is odd and its completey divisable by {1} and {2}".format(usrinp,divs1,divs2))

    elif (int(usrinp)%divs1 == 0) or (int(usrinp)%divs2 == 0):
        print("{0} is odd and its completely divisable by {1} or {2}\n next step we are identify the exact divisor".format(usrinp, divs1,divs2))
        if (int(usrinp)%divs1 == 0):
            print ("{0} is odd and its completely divisable by {1}".format(usrinp,divs1))
        elif (int(usrinp)%divs2 == 0):
            print ("{0} is odd and its completely divisable by {1}".format(usrinp,divs2))

    else:
        print ("{0} is odd and  its not compltely divisable by {1} and {2}".format(usrinp,divs1,divs2))

'''

# usk=input("Enter the Input\n")
# if (usk.isalpha()):
#     print ("{0} is alphabet".format(usk))
# elif (usk.isdigit()):
#     print ("{0} is number".format(usk))
# elif (usk.isalnum()):
#     print ("{0} contains alphabet and number".format(usk))

# usk=input("Enter the Input\n")
# if (usk.isalpha()):
#     print ("{0} is alphabet".format(usk))
#     print ("Enter '1' to convert to lowercase\n'2' to convert to uppercase\n'3' to swapcase")
#     usralop=input("Enter the user alphabet option")
#     if (usralop == "1"):
#         if (usk.islower()):
#             print ("{0} is already in lowercase".format(usk))
#         else:
#             print ("Converting {0} to lowercase in next step".format(usk))
#             conv_case=usk.lower()
#             if (conv_case.islower()):
#                 print ("{0} is successfully converted to lower".format(conv_case))
#     elif (usralop == "2"):
#         if (usk.isupper()):
#             print ("{0} is already in uppercase".format(usk))
#         else:
#             print ("{0} converting to uppercase".format(usk))
#             conv_upper=usk.upper()
#             if (conv_upper.isupper()):
#                 print ("{0} is successfully converted to uppercase".format(conv_upper))
#     elif (usralop == "3"):
#         print ("Swapping case of {0}".format(usk))
#         swap_out=usk.swapcase()
#         print ("Orginal input is {0} and swapped case is {1}".format(usk,swap_out))
#
# elif (usk.isdigit()):
#     print ("{0} is number".format(usk))
# elif (usk.isalnum()):
#     print ("{0} contains alphabet and number".format(usk))


# usk=input("Enter the Input\n")
# if (usk.isalpha()):
#     print ("{0} is alphabet".format(usk))
#     print ("Enter '1' to convert to lowercase\n'2' to convert to uppercase\n'3' to swapcase")
#     usralop=input("Enter the user alphabet option")
#     if (usralop == "1"):
#         if (usk.islower()):
#             print ("{0} is already in lowercase".format(usk))
#         else:
#             print ("Converting {0} to lowercase in next step".format(usk))
#             conv_case=usk.lower()
#             if (conv_case.islower()):
#                 print ("{0} is successfully converted to lower".format(conv_case))
#     elif (usralop == "2"):
#         if (usk.isupper()):
#             print ("{0} is already in uppercase".format(usk))
#         else:
#             print ("{0} converting to uppercase".format(usk))
#             conv_upper=usk.upper()
#             if (conv_upper.isupper()):
#                 print ("{0} is successfully converted to uppercase".format(conv_upper))
#     elif (usralop == "3"):
#         print ("Swapping case of {0}".format(usk))
#         swap_out=usk.swapcase()
#         print ("Orginal input is {0} and swapped case is {1}".format(usk,swap_out))
#
# elif (usk.isdigit()):
#     print ("{0} is number and its type is {1}\nto perform any mathematical we required int or float\n we are converting to int in next step".format(usk,type(usk)))
#     int_con=int(usk)
#     if (type(int_con) is int):
#         print ("We are successfully  converted  {0} to integer  and it type is {1}\npreviosuly its type was {2}".format(int_con,type(int_con),type(usk)))
#         n1=int(input("Enter numb1\n"))
#         n2=int(input("Enter the numb2\n"))
#         if (n1 == n2) and (n2==int_con) and (int_con == n1):
#             print ("All inputs are same and below are inputs provided\n{0}\n{1}\n{2}".format(int_con,n1,n2))
#         elif (n1 > n2) and (n2 < int_con):
#             print ("{0} is greater {1} but {1} is lesser than {2}".format(n1,n2,int_con))
#         elif (n1 == int_con) and (n2 != int_con):
#             print ("{0} and {1} are equal and {1} and {2} are not equal".format(n1,n2,int_con))
#
# elif (usk.isalnum()):
#     print ("{0} contains alphabet and number".format(usk))
#     anoj=input("Enter the another input\n")
#     fina_com=usk+"_"+anoj
#     print ("Combined {0} and {1} is {2}".format(usk,anoj,fina_com))
#     print ("/".join(fina_com))


