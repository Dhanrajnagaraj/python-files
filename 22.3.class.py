## ignoring perticular number of lines

no_line_ignored=int(input("Enter the number lines to be ignored"))
fileopen=open('F:\Suresh\\feb16.txt','r')
for j in range(0,no_line_ignored,1):
    fileopen.readline()

for con in fileopen:
    print (con.strip())



##=======================================================================
    

## printing line except perticular content
fileopen=open('F:\Suresh\\feb16.txt','r')
usrinpu=input("Enter the content")
for file_con in fileopen:
    if (file_con.strip() != usrinpu):
        print (file_con.strip())