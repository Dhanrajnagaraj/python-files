bh="pRaveenAjay saN12343___>>"
alp=[]
num=[]
spc=[]
for i in range(0,len(bh),1):
    if (bh[i].isalpha()):
        alp.append(bh[i])
        if (bh[i].isupper()):
            print ("{0} already in upper case".format(bh[i]))
        elif (bh[i].islower()):
            print ("{0} is in Lower case \n we will be converting to uppercase".format(bh[i]))
            conv=bh[i].upper()
            if (conv.isupper()):
                print ("{0} is successfully converted to upper".format(conv))


    elif (bh[i].isdigit()):
        num.append(bh[i])
        if (int(bh[i])%2 == 0):
            print ("{0} is completely divisbvale by 2".format(bh[i]))
        else:
            print ("{0} is not completely divisable by 2".format(bh[i]))
    elif (not bh[i].isalpha()) and (not bh[i].isdigit()):
        spc.append(bh[i])
    print ("===================================================")
print ("Alphabet details is {0}".format(alp))
print ("Number details is {0}".format(num))
print ("Special characters is {0}".format(spc))