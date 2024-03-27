#!/usr/bin/python
import os
filepath=input("Enter the Full path of file\n")
if os.path.isfile(filepath):
    print ("file {0} exsists".format(filepath))
else:
    print ("File {0} doesnt exsists".format(filepath))


#!/usr/bin/python
import os
content_present=[]
filepath=input("Enter the Full path of file\n")
if os.path.isfile(filepath):
    print ("file {0} exsists".format(filepath))
    con=input("Enter the content to be checked\n")
    fileopen=open('{0}'.format(filepath),'r')
    for filecheck_con in fileopen:
        if (con in filecheck_con):
            content_present.append(filecheck_con)
    if (len(content_present) > 0):
        print ("Content {0} present in file".format(con))
    else:
        print ("Content {0} not present in file".format(con))
else:
    print ("File {0} doesnt exsists".format(filepath))



#!/usr/bin/python
import os
content_present=[]
filepath=input("Enter the Full path of file\n")
if os.path.isfile(filepath):
    print ("file {0} exsists".format(filepath))
    con=input("Enter the content to be checked\n")
    fileopen=open('{0}'.format(filepath),'r')
    for filecheck_con in fileopen:
        if (con in filecheck_con):
            content_present.append(filecheck_con)
    if (len(content_present) > 0):
        line=0
        print ("Content {0} present in file".format(con))
        file_con_open=open('{0}'.format(filepath),'r')
        for mk in file_con_open:
            if (con in mk):
                line=line+1
                print ("{0} is present in Line number {1} of  file {2} ".format(mk.strip(),line,filepath))

    else:
        print ("Content {0} not present in file".format(con))
        con_add_recheck=[]
        file_write=open('{0}'.format(filepath),'a')
        file_write.write('\n')
        file_write.write(con)
        file_write.close()
        file_con_add_rec=open('{0}'.format(filepath),'r')
        for kl in file_con_add_rec:
            if (con in kl):
                con_add_recheck.append(con)
        if (len(con_add_recheck)>0):
            print ("Content {0} added sucessfully".format(con))
        else:
            print ("Content {0} not added sucessfully".format(con))
else:
    print ("File {0} doesnt exsists".format(filepath))


#!/usr/bin/python
import os
content_present=[]
filepath=input("Enter the Full path of file\n")
if os.path.isfile(filepath):
    print ("file {0} exsists".format(filepath))
    con=input("Enter the content to be checked\n")
    fileopen=open('{0}'.format(filepath),'r')
    for filecheck_con in fileopen:
        if (con in filecheck_con):
            content_present.append(filecheck_con)
    if (len(content_present) > 0):
        line=0
        print ("Content {0} present in file".format(con))
        file_con_open=open('{0}'.format(filepath),'r')
        for mk in file_con_open:
            line = line + 1
            if (con in mk):
                print ("{0} is present in Line number {1} of  file {2} ".format(mk.strip(),line,filepath))

    else:
        print ("Content {0} not present in file".format(con))
        con_add_recheck=[]
        file_write=open('{0}'.format(filepath),'a')
        file_write.write('\n')
        file_write.write(con)
        file_write.close()
        file_con_add_rec=open('{0}'.format(filepath),'r')
        for kl in file_con_add_rec:
            if (con in kl):
                con_add_recheck.append(con)
        if (len(con_add_recheck)>0):
            print ("Content {0} added sucessfully".format(con))
        else:
            print ("Content {0} not added sucessfully".format(con))
else:
    print ("File {0} doesnt exsists".format(filepath))




#!/usr/bin/python
import os
content_present=[]
filepath=input("Enter the Full path of file\n")
if os.path.isfile(filepath):
    print ("file {0} exsists".format(filepath))
    con=input("Enter the content to be checked\n")
    fileopen=open('{0}'.format(filepath),'r')
    for filecheck_con in fileopen:
        if (con in filecheck_con):
            content_present.append(filecheck_con)
    if (len(content_present) > 0):
        line=0
        print ("Content {0} present in file".format(con))
        file_con_open=open('{0}'.format(filepath),'r')
        for mk in file_con_open:
            line = line + 1
            if (con in mk):
                print ("{0} is present in Line number {1} of  file {2} ".format(mk.strip(),line,filepath))

    else:
        print ("Content {0} not present in file".format(con))
        con_add_recheck=[]
        user_optopn_lines=int(input("Enter the Number of lines to be added\n"))
        file_write=open('{0}'.format(filepath),'a')
        for j in range(0,user_optopn_lines,1):
            file_write.write('\n')
            cont_en=input("Enter the content to be added\n")
            file_write.write(cont_en)
        file_write.close()
        file_con_add_rec=open('{0}'.format(filepath),'r')
        for kl in file_con_add_rec:
            if (con in kl):
                con_add_recheck.append(con)
        if (len(con_add_recheck)>0):
            print ("Content {0} added sucessfully".format(con))
        else:
            print ("Content {0} not added sucessfully".format(con))
else:
    print ("File {0} doesnt exsists".format(filepath))




#!/usr/bin/python
import os
content_present=[]
filepath=input("Enter the Full path of file\n")
if os.path.isfile(filepath):
    print ("file {0} exsists".format(filepath))
    con=input("Enter the content to be checked\n")
    fileopen=open('{0}'.format(filepath),'r')
    for filecheck_con in fileopen:
        if (con in filecheck_con):
            content_present.append(filecheck_con)
    if (len(content_present) > 0):
        line=0
        print ("Content {0} present in file".format(con))
        file_con_open=open('{0}'.format(filepath),'r')
        for mk in file_con_open:
            line = line + 1
            if (con in mk):
                print ("{0} is present in Line number {1} of  file {2} ".format(mk.strip(),line,filepath))

    else:
        print ("Content {0} not present in file".format(con))
        con_add_recheck=[]
        user_optopn_lines=int(input("Enter the Number of lines to be added\n"))
        file_write=open('{0}'.format(filepath),'a')
        cont_en = input("Enter the content to be added\n")
        for j in range(0,user_optopn_lines,1):
            file_write.write('\n')
            file_write.write(cont_en)
        file_write.close()
        file_con_add_rec=open('{0}'.format(filepath),'r')
        for kl in file_con_add_rec:
            if (con in kl):
                con_add_recheck.append(con)
        if (len(con_add_recheck)>0):
            print ("Content {0} added sucessfully".format(con))
        else:
            print ("Content {0} not added sucessfully".format(con))
else:
    print ("File {0} doesnt exsists".format(filepath))
    file_createtest=open('{0}'.format(filepath),'w')
    con_lines=int(input("Enter the count of lines to be added\n"))
    for j in range(0,con_lines,1):
        con_not=input("Enter the content to be added\n")
        file_createtest.write(con_not)
    file_createtest.close()
    if os.path.isfile(filepath):
        print ("{0} got created sucessfully".format(filepath))
        print ("Below are Ffile content {0}".format(filepath))
        mlp=open('{0}'.format(filepath),'r')
        for hj in mlp:
            print (hj.strip())