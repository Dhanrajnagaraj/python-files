# #tuple example
# tu_ex=('man','apple','banana','orange','mango')
# print (type(tu_ex))
# fir=tu_ex[0]
# sec=tu_ex[1]
# out=fir+sec
# print (out)
#
# list=[]
# list.append(fir)
# list.append(sec)
# list.append(out)
# print (list)

newtuple=(['praveen','ajay','san'],['dhanjay','dhanraj','hitesh'],'hemanth',[10,20,30])
newlist=[]
firs=newtuple[1][1]
sec=newtuple[0][1]
thd=newtuple[2]
newlist.append(firs)
newlist.append(sec)
newlist.append(thd)
print (newlist)

#print (newtuple [-1::-1])
print (sum(newtuple[-1]))