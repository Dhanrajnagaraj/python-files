alist=['a','b','c']
blist=['10','2','3']
cdict={}
if (len(alist) == len(blist)):
    print ("Both Lists length are same")
    usrin=int(input("Enter '1' to covert to dictionary"))
    if (usrin == 1):
        for aran in range(0,len(alist),1):
            cdict[alist[aran]]=blist[aran]

else:
    print ("Both lists length are different")


print ("Dictionary details are {0}".format(cdict))


alist=['a','b','c']
blist=['10','2','3']
cdict={}
if (len(alist) == len(blist)):
    print ("Both Lists length are same")
    usrin=int(input("Enter '1' to covert to dictionary"))
    if (usrin == 1):
        for aran in range(0,len(alist),1):
            cdict[alist[aran]]=blist[aran]

else:
    print ("Both lists length are different")


print ("Dictionary details are {0}".format(cdict))

