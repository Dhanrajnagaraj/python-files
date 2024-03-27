## no of attempts to give user to enter input

usrattmp=int(input("Enter the number of attemepts allowed\n"))
try:
    n1=int(input("Enter the input"))
except Exception as e:
    print ("Invalid input provided and error is {0}, Next enter valid input".format(e))
    for j in range (1,usrattmp,1):
        print ("Attempt is {0} and remainining attempt is {1}".format(j,usrattmp-j))
        try:
            n1=int(input("Enter the input"))
            break
        except:
            pass
try:
    if (n1%2 == 0):
        print ("{0} is even".format(n1))
    else:
        print ("{0} is odd".format(n1))
except:
      print ("Input didnt capture since its not number")