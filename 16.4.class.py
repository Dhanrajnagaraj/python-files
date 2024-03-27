
alist=['a','b','c','d','e']
adict={'a':'10','b':'20','c':'30'}
dict_keys=list(adict.keys())
dict_values=list(adict.values())
print (dict_keys)
print (dict_values)

for list_item in alist:
    if (list_item in adict):
        print ("{0} present in dictionary".format(list_item))
        print ("key is {0} and its value is {1}".format(list_item,adict[list_item]))
    else:
        print ("{0} not present in dictionary\nNow we are trying to add".format(list_item))
        va_key=input("Enter the value\n")
        adict[list_item]=va_key
print (adict)



alist=['a','b','c','d','e']
adict={'a':'10','b':'20','c':'30','g':'88','z':'77'}
dict_keys=list(adict.keys())
dict_values=list(adict.values())
print (dict_keys)
print (dict_values)

for list_item in alist:
    if (list_item in adict):
        print ("{0} present in dictionary".format(list_item))
        adict.pop(list_item)

print (adict)
print (dir(adict))