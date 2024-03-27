####BOOLEAN OPERATION
'''
a="praveen"
print ('a' in a)
print ('k' in a)
print ('q' not in a)
print ('a' in a and 'z' in a)
print ('a' in a or 'z' in a)
print ('a' in a[2])
print ('e' in a[2] )

a="praveen"
b="kiran"
print (a[0] is a[-1])
print (a[0] is not a[-1])
print (a[0] == a[-1])
print (a[0] != a[-1])
print (a[4] is a[5])
print (len(a) == len(b))
print (len(a) != len(b))
usr_str=input("Enter the string to be checked\n")
inx_a=a.index(usr_str)
inx_b=b.index(usr_str)
print ("{0} is present position {1} in string {2}\n{0} is present position {3} in the string {4}".format(usr_str,inx_a,a,inx_b,b))
print (a[inx_a]==b[inx_b])
a="praveen"
b="kiran"
print (a[0] is a[-1])
print (a[0] is not a[-1])
print (a[0] == a[-1])
print (a[0] != a[-1])
print (a[4] is a[5])
print (len(a) == len(b))
print (len(a) != len(b))
usr_str=input("Enter the string to be checked\n")
inx_a=a.index(usr_str)
inx_b=b.index(usr_str)
print ("{0} is present position {1} in string {2}\n{0} is present position {3} in the string {4}".format(usr_str,inx_a,a,inx_b,b))
print (a[inx_a]==b[inx_b])



a="praveen"
b="kiran"
print (a[0] is a[-1])
print (a[0] is not a[-1])
print (a[0] == a[-1])
print (a[0] != a[-1])
print (a[4] is a[5])
print (len(a) == len(b))
print (len(a) != len(b))
usr_str=input("Enter the string to be checked\n")
inx_a=a.index(usr_str)
inx_b=b.index(usr_str)
print ("{0} is present position {1} in string {2}\n{0} is present position {3} in the string {4}".format(usr_str,inx_a,a,inx_b,b))
print (a[inx_a]==b[inx_b])
'''

'''
newlist=[]
a="praveen"
b="kiran"
pos=int(input("Enter the positio number\n"))
newc=a[pos]+b[pos]
print (newc)
newlist.append(newc)
print(newlist)
'''

'''
newlist=['praveen','ajay','san']
list2=['joy','fun','sana']

print (len(newlist) == len(list2))
print (len(newlist) == len(list2) and newlist[2] == list2[2])
print (len(newlist) == len(list2) and newlist[2] != list2[2])
print (len(newlist) == len(list2) and newlist[2] in list2[2])
print (len(newlist) == len(list2) and newlist[2] not in list2[2])
print (len(newlist) == len(list2) or newlist[2] in list2[2])
print (len(newlist[2]) > len(list2[2]))
print (len(newlist) > len(list2))
'''

'''
num1list=[10,20,30]             #without '' is integer
num2list=['10','20','30']       #with '' or "" is string
print (type(num1list[0]))
print (type(num2list[0]))
pos_num=int(input("Enter the position number\n"))
print ("{0} type is {1}\n {2} is {3}".format(num1list[pos_num],type(num1list[pos_num]),num2list[pos_num],type(num2list[pos_num])))

print (num1list[0]==num2list[0])

'''

'''
num2list=['10','20','30']
print (num2list[0].isdigit())
org=num2list[0]
int_con=int(org)
print ("orginal value {0} is in {1}\nPost coverting type is {2}".format(org,type(org),type(int_con)))
'''