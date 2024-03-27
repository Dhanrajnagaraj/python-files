def p1(a,b,c):
    d=a+b+c
    print (d)

usrchance=int(input("Enter the how many tries user can enter\n"))
try:
    n1=int(input("Enter the number1\n"))
except Exception as e:
    print ("Invalide input provided and error is {0}".format(e))
    for j in range(1,usrchance,1):
        try:
            print ("Try number : {0}".format(j))
            n1=int(input("Enter the number1\n"))
            break
        except:
            print ("Try number: {0} got failed".format(j))

try:
    n2=int(input("Enter the number2\n"))
except Exception as e:
    print ("Invalide input provided and error is {0}".format(e))
    for j in range(1,usrchance,1):
        try:
            print ("Try number : {0}".format(j))
            n2=int(input("Enter the number2\n"))
            break
        except:
            print ("Try number: {0} got failed".format(j))


n3=int(input("Enter the number3\n"))

p1(n1,n2,n3)
