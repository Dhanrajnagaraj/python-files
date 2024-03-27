import re
usrinput=input("Enter the main string\n")
subst=input("Enter the substring to be checked")
try:
    k=re.search(subst+'([0-9]{2})',usrinput)
    print (k.group())
except:
    print ("Pattern doesnt found\n")