## appending,removing items in list

a1=['praveenajay123','20','30','praveen','ajay','praveenajay','praveen123']
usrinp=input("Enter the input")
pos_cap=a1.index(usrinp)
print (pos_cap)
if (usrinp in a1):
    print ("{0} exsistsin list {1}".format(usrinp,a1))
    if (pos_cap == 0):
        print ("{0} item exsists in postion {1} in list {2}".format(usrinp,pos_cap,a1))
        if (usrinp.isalpha()):
            print (usrinp.swapcase())
        elif (usrinp.isdigit()):
            print ("{0} is number".format(usrinp))
            if(int(usrinp)%2 == 0):
                print ("{0} is even num".format(usrinp))
            else:
                print ("{0} is odd".format(usrinp))
        elif(usrinp.isalnum()):
            print ("{0} contains alphabet and number".format(usrinp))
            c=input("Enter the new input\n")
            new_out=usrinp+c
            a1[pos_cap]=new_out
            print (a1)

    elif (pos_cap == 1):
        print ("{0} exsisting in postion {1} in list {2}".format(usrinp,pos_cap,a1))
        print ("Removing position item {0}".format(pos_cap))
        del a1[pos_cap]
        print (a1)
    elif (pos_cap == 2):
        print("{0} exsisting in postion {1} in list {2}".format(usrinp, pos_cap, a1))
        a1.append(usrinp)
        print (a1)
    else:
        print ("{0} exists in list but not in position 0 1 2".format(usrinp))


