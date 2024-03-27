k=int(input("Enter the Number\n"))
evenlist=[]
oddlist=[]
for i in range(0,10,1):
    if (i%2 == 0):
        su=i+k
        print("{0} is even and incremented by {1} and output is {2}".format(i,k,su))
        evenlist.append(i)


    elif (i == 5) or (i == 7):
        mu=i*k
        print("Number is {0} and its multiplied by {1} and product is {2}".format(i,k,mu))

    elif (i%2 != 0):
        di=i-k
        print("Number {0}  is odd and its subtracted by {1} and difference is {2}".format(i,k,di))
        oddlist.append(i)

print ("Below are even list\n{0}".format(evenlist))
print ("Below are odd list\n{0}".format(oddlist))
