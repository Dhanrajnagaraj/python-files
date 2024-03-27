alist=['a','b','c','10']
blist=['d','e','f']
adict={'a':'10','b':'20','d':'praveen','e':'ajay123'}
bdict={'t':'pra','y':'een'}

usrinp=input("Enter the input\n")
if (usrinp in alist) and (usrinp in adict):
    print ("{0} present in {1}\n{0} present in {2}".format(usrinp,alist,adict))
    usrop=int(input("Enter '1' to display its position of list  and display its values\n'2' for removing item"))
    if (usrop == 1):
        itempo=alist.index(usrinp)
        print ("{0} exsisting in position {1} in list {2}\nKey is {0} and its value is {3} in {4}".format(usrinp,itempo,alist,usrinp,adict[usrinp],adict))
    elif (usrop == 2):
        print ("Removing {0} from list {1}".format(usrinp,alist))
        alist.remove(usrinp)
        print (alist)
        print ("REMOvING key {0} from dict {1}".format(usrinp,adict))
        adict.pop(usrinp)
        print (adict)

elif (usrinp in alist) and (usrinp not in adict):
    print ("{0} present in {1}\n{0} not present in {2}\nNow we are adding {0} to dictionary".format(usrinp,alist,adict))
    new_value=input("Enter the new value for key {0}\n".format(usrinp))
    adict[usrinp]=new_value
    print (adict)
elif (usrinp not in alist) and (usrinp in adict):
    print ("{0} not present in list {1}\npresent in {2}".format(usrinp,alist,adict))
    alist.append(usrinp)
    print (alist)

elif (usrinp not in alist) and (usrinp not in adict):
    print ("{0} not in {1}\n{0} not in {2}".format(usrinp,alist,adict))
    print ("Now we are copying list and dictionary")
    newlist=alist.copy()
    newdict=adict.copy()
    print ("new list is {0}".format(newlist))
    print ("New dictionary is {0}".format(newdict))
    print ("We are adding {0} to {1} list".format(alist,blist))
    blist.extend(alist)
    print (blist)
    print ("we are adding {0} to {1} dictionary".format(adict,bdict))
    bdict.update(adict)
    print (bdict)