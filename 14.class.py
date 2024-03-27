aco="kiran"
for i in aco:
    print (i)



aco="kiran"
len_aco=len(aco)
for i in range (0,len_aco,1);
    print ("{0} exits in position {1}".formate(aco[i],i))
    



aco="praveenajay"
len_aco=len(aco)
usri=input("Enter the character to be checked\n")
for i in range(0,len_aco,1):
    if (aco[i] == usri):
        print ("{0} exsists in position {1}".format(aco[i],i))




aco="praveenajay"
len_aco=len(aco)
usri=input("Enter the character to be checked\n")
if (usri in aco):
    print ("{0} exsists in {1}\nIn next step we are checking in which index position it exsists".format(usri,aco))
    for h in range(0,len_aco,1):
        if (aco[h] == usri):
            print ("{0} exsists in position {1}".format(aco[h],h))
else:
    print ("{0} doesnt exists in {1}".format(usri,aco))


aco="praveenajay"
len_aco=len(aco)
usri=input("Enter the character to be checked\n")
pos=int(input("Enter the Position number to be checked\n"))
if (usri in aco):
    print ("{0} exsists in {1}\nIn next step we are checking in which index position it exsists".format(usri,aco))
    for h in range(0,len_aco,1):
        if (h == pos) and (aco[pos] == usri):
                print ("{0} exsisting in Position number {1}".format(aco[pos],pos))
else:
    print ("{0} doesnt exists in {1}".format(usri,aco))


aco="praveenajaysanath"
vowel=[]
consonants=[]
vowelva="aeiou"
for i in range(0,len(aco),1):
    if (aco[i] in vowelva):
        vowel.append(aco[i])
    else:
        consonants.append(aco[i])
print ("Below are Vowel list\n{0}\nBelow are Consanatslist {1}".format(vowel,consonants))


aco=input("Enter the input\n")
vowel=[]
consonants=[]
vowelva="aeiou"
for i in range(0,len(aco),1):
    if (aco[i] in vowelva):
        vowel.append(aco[i])
    else:
        consonants.append(aco[i])
print ("Below are Vowel list\n{0}\nBelow are Consanatslist {1}".format(vowel,consonants))


bh="praveenajay san12343___>>"
alp=[]
num=[]
spc=[]
for i in range(0,len(bh),1):
    if (bh[i].isalpha()):
        alp.append(bh[i])
    elif (bh[i].isdigit()):
        num.append(bh[i])
    elif (not bh[i].isalpha()) and (not bh[i].isdigit()):
        spc.append(bh[i])
print ("Alphabet details is {0}".format(alp))
print ("Number details is {0}".format(num))
print ("Special characters is {0}".format(spc))