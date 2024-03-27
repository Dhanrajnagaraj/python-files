alist=[10,20,30,45,67,23,24]
evenpositionlist=[]
oddpositionlist=[]
evennumberposition_oddnumber=[]
evennumberposition_evebnumber=[]
oddnumberposition_oddnumber=[]
oddnumberposition_evennumber=[]
oddnumber=[]
evennumber=[]
subtracted_from_even=[]
added_from_odd=[]
def evenposition_capture():
    evenpositionlist.append(alist[i])
    even_number()



def oddposition_capture():
    oddpositionlist.append(alist[i])
    odd_number()

def odd_number():
    if (alist[i]%2 != 0):
        oddnumber.append(alist[i])
        out=alist[i]+usr
        added_from_odd.append(out)
def even_number():
    if (alist[i]%2 == 0):
        evennumber.append(alist[i])
        outp=alist[i]-usr
        subtracted_from_even.append(outp)

usr=int(input("Enter the number\n"))
for i in range(0,len(alist),1):
    if (i%2 == 0):
        evenposition_capture()
    elif (i%2 != 0):
        oddposition_capture()

print ("Below are even positioned list\n{0}\nBelow are odd positioned list \n{1}".format(evenpositionlist,oddpositionlist))
print ("Below are even number items\n{0}\nBelow are odd number items\n{1}".format(evennumber,oddnumber))
print ("Below are the subtacted list from even\n{0}\nBelow are added lits from odd\n{1}".format(subtracted_from_even,added_from_odd))