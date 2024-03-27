import re
userinputstring=input("Enter the main string\n")
string1=input("Enter the first string\n")
string2=input("Enter the second string\n")
search_element=re.compile(r'{0}|{1}'.format(string1,string2))
try:
    ser=re.search(search_element,userinputstring)
    print (ser.group())
except:
    print ("Pattern doesnt exsists")


#=========================================================================

import re
userinputstring=input("Enter the main string\n")
string1=input("Enter the first string\n")
string2=input("Enter the second string\n")
search_element=re.compile(r'{0}|{1}'.format(string1,string2))
try:
    ser=re.search(search_element,userinputstring)
    outele=ser.group()
    if (outele == string1):
        print ("first element {0} is printing".format(string1))
    elif (outele == string2):
        print ("Second element {0} is printing".format(string2))
except:
    print ("Pattern doesnt exsists")

#==========================================================================

import re
userinputstring=input("Enter the main string\n")
string1=input("Enter the first string\n")
string2=input("Enter the second string\n")
elemen1=re.compile(r'{0}'.format(string1))
elemen2=re.compile(r'{0}'.format(string2))
#search_element=re.compile(r'{0}'.format(string1)) and re.compile(r'{0}'.format(string2))
try:
    ser=re.search(elemen1,userinputstring) and re.search(elemen2,userinputstring)
    print (ser.group())
except:
    print ("Pattern doesnt exsists")