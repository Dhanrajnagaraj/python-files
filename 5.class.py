listexample=['praveen','ajay','ajit','shri','kiran']
listexample2=['a','b','c','d']

listexample.extend(listexample2)
print(listexample)

listexample.sort()
print (listexample)

listexample.reverse()
print (listexample)
listexample.remove('ajit')
print (listexample)

oplist=[12,4,123,4,34,24]
# print(oplist)
# oplist.sort()
# print(oplist)
# oplist.sort(reverse=True)
# #print(oplist)
# print(oplist[0] +  oplist[1])
#
# oplist=[45,2,67,1,87]
# print (oplist)
# finallist=[]
# firg=int(input("Enter the Position\n"))
# secondg=int(input("Enter the position\n"))
# addout=oplist[firg]+oplist[secondg]
# subg=oplist[firg]-oplist[secondg]
# prodg=oplist[firg]*oplist[secondg]
# finallist.append(addout)
# finallist.append(subg)
# finallist.append(prodg)
# print (finallist)
#
# copylist=finallist.copy()
# print (copylist)


listexample=['praveen','ajay','ajit','shri','kiran']
listexample.insert(3,'india')
print (listexample)
listexample.pop()
print (listexample)
listexample.clear()
print (listexample)
