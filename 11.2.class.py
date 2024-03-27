## if contion in dictionary

adict={'a':'10','b':'ajay','c':'san','d':'30'}
alist=['10','ajay']
keylist=list(adict.keys())
valuelist=list(adict.values())
print (keylist)
print (valuelist)
usrkey=input("Enter the keybname\n")
if (usrkey in adict):
    print ("Key {0} present in dictionary{1}".format(usrkey,adict))
    print (adict[usrkey])
elif (usrkey not in adict):
    print ("Key {0} not in dictionary {1}".format(usrkey,adict))
    newvalue=input("Enter the value\n")
    adict[usrkey]=newvalue
    print (adict)