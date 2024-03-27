import re
usrinput=input("Enter the userinput\n")
com_check=re.compile(r'[a-z]')
try:
    ko=re.search(com_check,usrinput)
    print (ko.group())
except:
    print ("Pattern doesnt found")

#===============================================

import re
usrinput=input("Enter the userinput\n")
com_check=re.compile(r'[a-z0-9A-Z]')
try:
    ko=re.search(com_check,usrinput)
    print (ko.group())
except:
    print ("Pattern doesnt found")

#================================================
    
import re
usrinput=input("Enter the userinput\n")
com_check=re.compile(r'[a-z]')
com1_check=re.compile(r'[0-9]')

try:
    ko=re.search(com1_check,usrinput) and re.search(com_check,usrinput)
    print (ko.group())
except:
    print ("Pattern doesnt found")

#=================================================
    
import re
usrinp=input("Enter the userinput\n")
subst=input("Enter the substring\n")
mk=re.compile(r'{0}[0-9][0-9]'.format(subst))
try:
    lp=re.search(mk,usrinp)
    print (lp.group())
except:
    print ("{0} pattern doesnt found".format(mk))