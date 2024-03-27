#!/usr/bin/python

import subprocess
import os
import re
import datetime
usrfilecontent=[]
usropt=raw_input("Enter '1' to Check user present or not\n'2' if user not present it should create user and verify\n'3' if user prent enter '1' to add user to grp '2' to delete user")
usrcheck=raw_input("Enter the username to be checked\n")
userfile=open('/etc/passwd','r')
for usr_fil in userfile:
        usrfilecontent.append(usr_fil)
#print (usrfilecontent)
user_present_conf=[]
for usr_check_p in usrfilecontent:
        usre_spliteed=usr_check_p.strip().split(':')
        if (usre_spliteed[0] == usrcheck):
                user_present_conf.append('present')

print (user_present_conf)
if (len(user_present_conf) > 0):
        print ("{0} present in server".format(usrcheck))
        cmd="chage -l {0}".format(usrcheck)
        cmd_exec=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]
        print (cmd_exec)
else:
        print ("{0} Not present in server".format(usrcheck))
        os.system("useradd {0}".format(usrcheck))
        user_check_post_create="grep {0} /etc/passwd".format(usrcheck)
        user_check_con=subprocess.Popen(user_check_post_create,stdout=subprocess.PIPE,shell=True).communicate()[0]
        splitted_user_check=user_check_con.strip().split(':')
        if (splitted_user_check[0] == usrcheck):
                print ("User {0} got created successfully".format(usrcheck))
        else:
                print ("User {0} not created successfully".format(usrcheck))


#!/usr/bin/python
import subprocess
import os
import re
import datetime
usrfilecontent=[]
usropt=raw_input("Enter '1' to Check user present or not\n'2' if user not present it should create user and verify\n'3' if user prent enter '1' to add user to grp '2' to delete user")
usrcheck=raw_input("Enter the username to be checked\n")
userfile=open('/etc/passwd','r')
for usr_fil in userfile:
        usrfilecontent.append(usr_fil)
#print (usrfilecontent)
user_present_conf=[]
for usr_check_p in usrfilecontent:
        usre_spliteed=usr_check_p.strip().split(':')
        if (usre_spliteed[0] == usrcheck):
                user_present_conf.append('present')

print (user_present_conf)
if (len(user_present_conf) > 0):
        print ("{0} present in server".format(usrcheck))
        cmd="chage -l {0}".format(usrcheck)
        cmd_exec=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]
        print (cmd_exec)
        user_opt_add_delete=raw_input("Enter '1' to add user to group\n'2' to delete user")
        if (user_opt_add_delete == "1"):
                grpname=raw_input("Enter the Groupname\n")
                cmd_usre_grp="usermod -G {0} {1}".format(grpname,usrcheck)
                subprocess.Popen(cmd_usre_grp,stdout=subprocess.PIPE,shell=True).communicate()
                cmd_check_user_grp="groups {0}".format(usrcheck)
                cmd_check_user_grp_exec=subprocess.Popen(cmd_check_user_grp,stdout=subprocess.PIPE,shell=True).communicate()[0]
                if (grpname in cmd_check_user_grp_exec):
                        print ("{0} Part of Group {1}".format(usrcheck,grpname))
                else:
                        print ("{0} Not part of Group {1}".format(usrcheck,grpname))
        elif (user_opt_add_delete  == "2"):
                os.system("userdel {0}".format(usrcheck))
                cmd_check_dele="grep {0} /etc/passwd".format(usrcheck)
                cmd_check_dele_exec=subprocess.Popen(cmd_check_dele,stdout=subprocess.PIPE,shell=True).communicate()
                userdel_con=cmd_check_dele_exec[0]
                if (len(userdel_con)>0):
                        print ("User {0} Not deleted".format(usrcheck))
                else:
                        print ("User {0} Got deleted".format(usrcheck))
else:
        print ("{0} Not present in server".format(usrcheck))
        os.system("useradd {0}".format(usrcheck))
        user_check_post_create="grep {0} /etc/passwd".format(usrcheck)
        user_check_con=subprocess.Popen(user_check_post_create,stdout=subprocess.PIPE,shell=True).communicate()[0]
        splitted_user_check=user_check_con.strip().split(':')
        if (splitted_user_check[0] == usrcheck):
                print ("User {0} got created successfully".format(usrcheck))
        else:
                print ("User {0} not created successfully".format(usrcheck))


#!/usr/bin/python
import subprocess
import re
import os
import datetime
respace=re.compile(r'\s+')
cmd="free"
sub_cmmd=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0].split('\n')
ramdetails=sub_cmmd[1]
print (ramdetails)
remos=re.sub(respace," ",ramdetails).split(' ')
print (remos)
totalram=remos[1]
usedram=remos[2]
freeram=remos[3]
print (float(freeram)/float(totalram))
total_free_perce=(float(freeram)*100/float(totalram))
print (total_free_perce)
if (total_free_perce < 90):
        print ("Memory Utilization crossed Threshold and Below are process consuming most of memory")
        cmd_mem="ps axo %mem,user,pid,command|sort -k1 -nr | head -10"
        print (subprocess.Popen(cmd_mem,stdout=subprocess.PIPE,shell=True).communicate()[0])

else:
        print ("Memory Utilization below threhso;d no issues")
