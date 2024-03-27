import re
pat=re.compile(r'[0-9]{2}')
fileopen=open('D:\Python_test_file\\test_regular_express.txt','r')
for i in fileopen:
    if re.search(pat,i):
        print (i.strip())


import re
pat=re.compile(r'kiran')
fileopen=open('D:\\python_test.txt','r')
for i in fileopen:
    if re.search(pat,i):
        print (i.strip())


#=============================================================================
        
import re
pat=re.compile(r'praveen')
fileopen=open('D:\Python_test_file\\test_regular_express.txt','r')
filewrite=open('D:\Python_test_file\\praveenconte.txt','w')        ## creating file and writing in that file
for i in fileopen:
    if re.search(pat,i):
        print (i.strip())
        filewrite.write(i)

===================================================
import re
pat=re.compile(r'Kiran[0-9]{2}')                ## after name 2 digit must
fileopen=open('D:\\python_test.txt','r')
for i in fileopen:
    if re.search(pat,i):
        print (i.strip())

===================================================
import re
pat=re.compile(r'^Kiran[0-9]{2}') ## name start Kiran and 2 digit must
fileopen=open('D:\\python.txt','r')

for i in fileopen:
    if re.search(pat,i):
        print (i.strip())

====================================================
import re
pat=re.compile(r'^Kiran[0-9]{2}$') ## name start Kiran and 2 digit must and end with same
fileopen=open('D:\\python.txt','r')

for i in fileopen:
    if re.search(pat,i):
        print (i.strip())


===================================================

import re
fileopen=open('D:\\python_test.txt','r')
pat=re.compile(r'praveen')
for h in fileopen:
    if not re.search(pat,h):  ## line not contain praveen
        print (h.strip())


import re
fileopen=open('D:\Python_test_file\\test_regular_express.txt','r')
pat=re.compile(r'praveen',re.IGNORECASE)  ## ignoring case-sensitive(ignoring small and capital letters)
for h in fileopen:
    if not re.search(pat,h):
        print (h.strip())



========================================================

import re
pat=re.compile(r'[0-9]\.[0-9]\.[0-9]\.[0-9]')  ## fetching ips from the file 
fileopen=open('D:\Python_test_file\\test_regular_express.txt','r')

for lp in fileopen:
    if re.search(pat,lp):
        print (lp.strip())
=================================
import re
pat=re.compile(r'[0-9]{3}\.[0-9]{3}\.[0-9]{2}\.[0-9]{1')  ## fetching ips from the file 
fileopen=open('D:\Python_test_file\\test_regular_express.txt','r')

for lp in fileopen:
    if re.search(pat,lp):
        print (lp.strip())
================================

## printing ips
import re
pat=re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')  ## fetching ips from the file 
fileopen=open('D:\Python_test_file\\test_regular_express.txt','r')

for lp in fileopen:
    if re.search(pat,lp):
        print (lp.strip())

================================

## printing valid ip (file contain 12.12.400.454 it is invalid ip)

import re
pat=re.compile(r'[0-2][0-9]{1,2}\.[0-2][0-9]{1,2}\.[0-2][0-9]{1,2}\.[0-2][0-9]{1,2}')  ## fetching ips from the file 
fileopen=open('D:\Python_test_file\\test_regular_express.txt','r')

for lp in fileopen:
    if re.search(pat,lp):
        print (lp.strip())

##=========================================OR===================================

import re
pat=re.compile(r'[0-2]?[0-9]{1,2}\.[0-2]?[0-9]{1,2}\.[0-2]?[0-9]{1,2}\.[0-2]?[0-9]{1,2}')  ## fetching valid ips from the file
fileopen=open('D:\\python_test.txt','r')

for lp in fileopen:
    if re.search(pat,lp):
        print (lp.strip())

