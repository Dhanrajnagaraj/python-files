divisor=int(input("Enter the Divisor for odd number\n"))

#odd_divisable="odd_divisable_by_{0}".format(divisor)
evenlist=[]
oddlist=[]
odd_divisable_final=[]
odd_but_not_divisabkle_final=[]
for i in range(0,30,1):
    if (i%2 == 0):

        #print("{0} is even".format(i))
        evenlist.append(i)

    elif (i%2 != 0):
        oddlist.append(i)

        if (i%divisor == 0):
            #print ("{0} is odd but its completely divisable by {1}".format(i,divisor))
            odd_divisable_final.append(i)
        elif (i%divisor != 0):
            #print ("{0} is odd but its not completely divisable by {1}".format(i,divisor))
            odd_but_not_divisabkle_final.append(i)


print ("Below are the Even number\n{0}".format(evenlist))
print ("Below are the Odd number\n{0}".format(oddlist))
print ("Below are the odd number which is completey divisvale by {0}\n{1}".format(divisor,odd_divisable_final))
print ("Below are the odd number which is not completey divisvale by {0}\n{1}".format(divisor,odd_but_not_divisabkle_final))
