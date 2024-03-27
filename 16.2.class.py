alist=['praveen','ajay','san','praveen','kiran','vijay','ajay']
nonduplicate=[]
capturing_repeated_item=[]
for itn in alist:
    if itn not in nonduplicate:
        nonduplicate.append(itn)
for nonp in nonduplicate:
    co_occ=alist.count(nonp)
    if (co_occ>1):
        capturing_repeated_item.append(nonp)
print ("{0} occurs {1} times in list {2}".format(capturing_repeated_item[0],alist.count(capturing_repeated_item[0] ),alist))
print ("Below are items which got repated more than 1 times\n{0}".format(capturing_repeated_item))

