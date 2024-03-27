len_lis_th=int(input("Enter the length of list\n"))
item_len_th=int(input("Enter the itemlength"))
alist=['praveen','ajay','sanabhiajay','kirana','dhanraj']
if (len(alist)>len_lis_th):
    print ("Lenghtb of items is greater than {0}".format(len_lis_th))
    for itm in alist:
        item_len=len(itm)
        if (item_len > item_len_th):
            cha_cha=input("Enter the characted to be checked\n")
            if (cha_cha in itm):
                break
            else:
                print (itm)
        else:
            print (itm)
else:
    print ("Length of items in list is lesser than {0}".format(len_lis_th))
    usr_app=input("Enter the item to be appended\n")
    alist.append(usr_app)
    print (alist)