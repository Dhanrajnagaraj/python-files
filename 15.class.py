list1['kiran','ajit','10','20']
for i in range (0,len(list1),2)
 print (list1[i])

 ============================================

 list1=['praveen','ajay','san','abhi','praveen123','ajay123']
usr=input("Enter the User input\n")
post=int(input("Enter the Position Number\n"))
if usr in list1:
    print ("{0} present in List {1}".format(usr,list1))
else:
    print ("{0} not present in list {1}".format(usr,list1))



=============================================


list1=['kiran','ajit','10','20']
for i in range (0,len(list1),2):
 print (i,list1[i])

=============================================

list1=['kiran','ajit','10','20']
usri=input("Enter the user name\n") 
if (usri in list1):
    for j in range(0,len(list1),1):
        if (list1[j] == usri):
            print ("{0} present in Position {1} in list {2}".format(usri,j,list1))
else:
    print ("{0} Not present in list {1}\nAdding {0} to list {1}".format(usri,list1))
    list1.append(usri)
    print (list1)


==============================================

list1=['praveen','ajay','praveen123','ajay','abhi','kiran']
usri=input("Enter the user input\n")
pos=int(input("Enter the Position Number\n"))
if (usri in list1):
    for j in range(0,len(list1),1):
        if ( j == pos):
            if (list1[j] == usri):
                print ("{0} present in position {1} in list {2}".format(usri,j,list1))
            else:
                print ("{0} not Present in position {1} in list {2}".format(usri,j,list1))

else:
    print ("{0} Not present in list {1}\nAdding {0} to list {1}".format(usri,list1))
    list1.append(usri)
    print (list1)

================================================    

list1=['praveen','ajay','praveen123','ajay','abhi','kiran']
usri=input("Enter the user input\n")
pos=int(input("Enter the Position Number\n"))
if (usri in list1):
    for j in range(0,len(list1),1):
        if ( j == pos):
            if (list1[j] == usri):
                print ("{0} present in position {1} in list {2}".format(usri,j,list1))
            else:
                print ("{0} not Present in position {1} in list {2}\n{0} present in Position {3}\nNow updating {0} in {4}".format(usri,j,list1,list1.index(usri),pos))
                list1[pos]=usri
                print (list1)

else:
    print ("{0} Not present in list {1}\nAdding {0} to list {1}".format(usri,list1))
    list1.append(usri)
    print (list1)

===================================================

flist=['praveen','ajaypraveen','sanabhi','kiranajay','akash','hitesh']
len_th=int(input("Enter the length to be checked\n"))
not_macthed_lenght=[]
for i in flist:
    if (len(i) > len_th):
        print ("{0} length is {1} and its position is {2}".format(i,len(i),flist.index(i)))
    else:
        print ("{0} length is lesser or equl ti {1}".format(i,len_th))
        not_macthed_lenght.append(i)
print ("Below are details of listitems whose length is lesser than {0}\n{1}".format(len_th,not_macthed_lenght))

====================================================

flist=['praveen','ajaypraveen','sanabhi','kiranajay','akash','hitesh']
len_th=int(input("Enter the length to be checked\n"))
not_macthed_lenght=[]
matched_length=[]
exact_length=[]
for i in flist:
    if (len(i) > len_th):
        print ("{0} length is {1} and its position is {2}".format(i,len(i),flist.index(i)))
        matched_length.append(i)
    elif (len(i) == len_th):
        exact_length.append(i)
    else:
        print ("{0} length is lesser or equl ti {1}".format(i,len_th))
        not_macthed_lenght.append(i)
print ("Below are details of listitems whose length is lesser than {0}\n{1}".format(len_th,not_macthed_lenght))
print ("Below are details of listitems whose length is greater than {0}\n{1}".format(len_th,matched_length))
print ("Below are details of listitems whose length is exactly {0}\n{1}".format(len_th,exact_length))

====================================================




