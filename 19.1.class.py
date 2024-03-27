alist=[10,20,30,45,67,23,24]
evenpositionlist=[]
oddpositionlist=[]
evennumberposition_oddnumber=[]
evennumberposition_evebnumber=[]
oddnumberposition_oddnumber=[]
oddnumberposition_evennumber=[]

def evenposition_capture():
    evenpositionlist.append(alist[i])


def oddposition_capture():
    oddpositionlist.append(alist[i])


for i in range(0,len(alist),1):
    if (i%2 == 0):
        evenposition_capture()
    elif (i%2 != 0):
        oddposition_capture()

print ("Below are even positioned list\n{0}\nBelow are odd positioned list \n{1}".format(evenpositionlist,oddpositionlist))