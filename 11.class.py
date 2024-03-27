a1=['10','20','30','praveen','kiran']
pos_in=int(input("Enter the Position number\n"))
e1=input("Enter the first element\n")
e2=input("Entere the second element\n")
if (a1[pos_in] == e1 or a1[pos_in] == e2 ):
    print ("Elemet {0} or {1} exsists in position {2}".format(e1,e2,pos_in))
    if (e1 in a1[pos_in]):
        print ("elements {0} exsist in position {1} in list {2} and we are updating the position value".format(e1,pos_in,a1))
        new_value=input("Enter the new value\n")
        a1[pos_in]=new_value
        print ("Below are details of list post updating {0} in post {1}".format(new_value,pos_in))
        print (a1)
    elif (e2 in a1[pos_in]):
        print ("elemenet {0} exsists in postion {1} in list {2}\nwe are removing item {0} ".format(e2,pos_in,a1))
        a1.remove(e2)
        print (a1)
elif (a1[pos_in] != e1 and a1[pos_in] != e2 ):
    anot=input("Enter the new element to add to list")
    a1.append(anot)
    print (a1)
