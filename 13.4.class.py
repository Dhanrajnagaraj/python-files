inp=int(input("Enter the Input number\n"))
for i in range(0,50,1):
    if (i>0) and (i<15):
        print("number {0} between 0 and 15".format(i))
        su=i+inp
        print ("Orginal number is {0} and incdemented by {1} and sum is {2}".format(i,inp,su))
    elif ( i == 15) or (i == 40):
        print ("Orginal number is {0} and praveen".format(i))
    elif (i>15) and (i<40):
        print ("Number {0} between 15 and 40".format(i))
        mu=i*inp
        print ("Oginal number is {0} and multipled by {1} and prodict is {2}".format(i,inp,mu))
    elif (i>40) and (i<50):
        print ("Number {0} betweeen 40 and 50".format(i))
        di=i-inp
        print ("Orginla numner is {0} and subtracted by {1} and differe nce is {2}".format(i,inp,di))







