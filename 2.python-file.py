#!/usr/bin/python
'''
a="abcdefghijklmnopqrstuvwxyz"
print (a)
print (len(a))
print (a[0::2])
print (len(a[0::2]))



a="praveenajay"
b="san"
a_len=len(a)
b_len=len(b)
c=a+b
print (type(a))
print ("Input is {0} and length is {1} and its datatype is {2}".format(a,a_len,type(a)))
print ("Input is {0} and length is {1} and its datatype is {2}".format(b,b_len,type(b)))
print ("Input is {0} and length is {1} and its datatype is {2}".format(c,len(c),type(c)))
print ("=====================================================")
print ("Input is {0} and length is {1} and its datatype is {2}\nInput is {3} and length is {4} and its datatype is {5}\nInput is {6} and length is {7} and its datatype is {8}".format(a,a_len,type(a),b,b_len,type(b),c,len(c),type(c)))
'''

'''
a="kiran"
b="shri"
usr=input("Enter the input\n")
print (usr)
lp=a+b+usr
print (lp)
len_lp=len(lp)
str=int(input("Enter the startpoint\n"))
#endpo=int(input("Enter the endpoint\n"))
#jumppo=int(input("Enter jump-point\n"))
#print (lp[str:endpo:jumppo])
end_po_sun=int(input("Enter the number tobe substracted from lenght"))
print (lp[str:len_lp-end_po_sun])
'''

'''
a="      kiran ajay shri      "
print (len(a))
re_sp=a.strip()
print (len(re_sp))
space_removed=len(a)-(len(re_sp))
print ("Extra space removed is {0}".format(space_removed))
'''

'''
a="ajaykiransanbesan_dhanraj"
ininp=input("Enter the character to be checked for index poistion\n")
indpo=a.index(ininp)
print ("Character {0} present at position {1} in the string {2} and its length is {3}".format(ininp,indpo,a,len(a)))
'''

'''
#separater_eg
a="kiran_shri_om_raju_amit"
b=a.split('_') #('a') ('o')
print (b)
'''

'''
#joing_eg
a="praveen"
hu="_".join(a)   #joining _ after each letter
print (hu)
'''

# #Number add
# n1=int(input("Enter the num1\n"))
# n2=int(input("Enter the num2\n"))
# sumr=n1+n2
# diffh=n1-n2
# prod=n1*n2
#
# print ("Sum of {0} and {1} is {2}".format(n1,n2,sumr))
# print ("Sum of {0} and {1} is {2}".format(n1,n2,diffh))
# print ("Sum of {0} and {1} is {2}".format(n1,n2,prod))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [{'a': '123'}]
print(b)
