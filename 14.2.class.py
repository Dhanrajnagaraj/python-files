list1=['kiran','ajit','shri','om','10','20']
for i in list1:
    print (i)


list1=['kiran','ajit','shri','om','10','20']
for i in range (0,len(list1),1):
    print ("{0} is present in position {1}".format(list1[i],i))



for i in range(0,len(list1),1):
    if (i%2 == 0):
        even_pos.append(list1[i])
    elif(i%2 != 0):
        odd_pos.append(list1[i])
print ("Below are Even numbered Positio list\n{0}\nBelow are Odd numbered position list {1}".format(even_pos,odd_pos))



list1=['praveen','ajay','11','20','30']
even_pos=[]
odd_pos=[]

for i in range(0,len(list1),1):
    if (i%2 == 0):
        print ("{0} is even position".format(list1[i]))
        even_pos.append(list1[i])
        if (list1[i].isalpha()):
            alin=input("Enter the new input\n")
            new_inp_1=list1[i]+alin
            list1.append(new_inp_1)
        elif (list1[i].isdigit()):
            if (int(list1[i])%2 == 0):
                print ("{0} is even number".format(list1[i]))
            else:
                print("{0} is odd number".format(list1[i]))
    elif(i%2 != 0):
        odd_pos.append(list1[i])
print ("Below are Even numbered Positio list\n{0}\nBelow are Odd numbered position list {1}".format(even_pos,odd_pos))


print (list1)