## local and global variables

def p1():
    s="KIRAN"
    print (s)

s="ajay"
print ("outside of function")
print (s)                                         ## print ajay
print ("Now we are calling the function")
p1()                                              ## print KIRAN
print ("post calling functions")
print(s)                                          ##print ajay

===========================================================================



## global variable

def p1():
    global s
    s="KIRAN"
    print (s)

s="ajay"
print ("outside of function")
print (s)                                         ## print ajay
 ## after this "s" will be function because we use global variables
print ("Now we are calling the function")
p1()                                              ## print KIRAN
print ("post calling functions")
print(s)                                          ##print KIRAN




