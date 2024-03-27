alist=['praveen','ajay','san']
blist=['ajay','abhi','giri','vijay']
present_list=[]
notpresent_list=[]
for aran in range(0,len(alist),1):
    if (alist[aran] in blist):
        for bran in range(0,len(blist),1):
            if (alist[aran] == blist[bran]):
                print ("{0} present in position {1} in {2}".format(alist[aran],aran,alist))
                print ("{0} present in position {1} in {2}".format(blist[bran],bran,blist))
                present_list.append(blist[bran])
    else:
        print ("{0} not present in {1}".format(alist[aran],blist))
        notpresent_list.append(alist[aran])
print ("common elements in both list\n{0}".format(present_list))
print ("Not presnet in {0}\n{1}".format(blist,notpresent_list))