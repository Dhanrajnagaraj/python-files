alist=['praveen','ajay','san','praveen','kiran','vijay','ajay']
nonduplicate=[]
for itn in alist:
    if itn not in nonduplicate:
        nonduplicate.append(itn)
print ("Below are items of list post removing duplicates\n{0}".format(nonduplicate))




alist=['praveen','ajay','san','praveen','kiran','vijay','ajay']
nonduplicate=[]
for itn in alist:
    if itn not in nonduplicate:
        nonduplicate.append(itn)
for nonp in nonduplicate:
    co_occ=alist.count(nonp)
    if (co_occ > 1):
        print ("{0} occurs {1} times in list {2}".format(nonp,co_occ,alist))


alist=['praveen','ajay','san','praveen','kiran','vijay','ajay']
nonduplicate=[]
for itn in alist:
    if itn not in nonduplicate:
        nonduplicate.append(itn)
for nonp in nonduplicate:
    co_occ=alist.count(nonp)
    if (co_occ > 1):
        print ("{0} occurs {1} times in list {2}".format(nonp,co_occ,alist))