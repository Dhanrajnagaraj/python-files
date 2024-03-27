## checking content present in the file or not 


fileopen=open('F:\Suresh\\feb16.txt','r')
final_file_content=[]                          ## out put of the file stot=redin this variable
filecont=fileopen.readlines()
for j in filecont:
    final_file_content.append(j.strip())
print (final_file_content)
usrinput=input("Enter the content to be checked")
if (usrinput in final_file_content):
    capt = final_file_content.index(usrinput)               ## with index we finding which line content present
    print ("Content {0} present in file and its in line number {1}".format(usrinput,capt+1))

else:
    print ("Content {0} not present in file".format(usrinput))


=========================================OR======================================================


fileopen=open('F:\Suresh\\feb16.txt','r')
final_file_content=[]
filecont=fileopen.readlines()
for j in filecont:
    final_file_content.append(j.strip())
print (final_file_content)
usrinput=input("Enter the content to be checked")
if (usrinput in final_file_content):
    print ("Content {0} present in file".format(usrinput))
    for k in range(0,len(final_file_content),1):               ## with for loop we can check the content in which line
        if (final_file_content[k] == usrinput):
            print ("{0} present in line number {1}".format(usrinput,k+1))
else:
    print ("Content {0} not present in file".format(usrinput))
