## file system in python

fileopen=open('D:\\python_test.txt','r')

print (fileopen.readline())   ## only print 1st line

for i in fileopen:
    print(i.strip())          ## read line by line


print (fileopen.readlines()) ## out put in format of list



==========================================================================


usrinput=input("Enter the userinput\n")
fileopen=open('D:\\python_test.txt','r')
j=0
for i in fileopen:
    j=j+1
    if (usrinput == i.strip()):
        print ("{0} present in file and in linenumber {1}".format(usrinput,j))