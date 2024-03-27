## linux and python automation

#!/bin/bash/python
import os                   ## in os module we cant store value as avariable
print(os.system("uptime;uname"))



#!/usr/bin/python
import subprocess   ## with this we can store a value in variable
cmd="uptime"
exe_cmd=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()
print (exe_cmd[0])


#!/usr/bin/python
import subprocess
import re
usrinput=raw_input("Enneter '1' to know installation date\n'2' to check particular present or not\n'3'would like find how many times particular users logged in till now\n'4'would like display ram details\n'5' display only swap details")
if (usrinput  == "1"):
        cmd="last"
        last_exe=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]
        final_last=last_exe.strip().split('\n')
        for opi in final_last:
                if "wtmp" in opi:
                        print ("Below is the Installation date of server\n{0}".format(opi))
elif (usrinput == "2"):
        usrname=raw_input("Enter the username\n")
        usr_com=re.compile(r'^{0}'.format(usrname))
        exact_us=re.compile(r'^{0}$'.format(usrname))
        file_open=open('/etc/passwd','r')
        for mk in file_open:
                if re.search(usr_com,mk):
                        splitted_out=mk.split(':')
                        home=splitted_out[-2]
                        shell_user=splitted_out[-1]
                        if re.search(exact_us,splitted_out[0]):
                                print ("Below are the details of user {0}\nUsername={0}\nHome directory={1}\nShell={2}".format(usrname,home,shell_user))
                                cmd_ch="chage -l {0}".format(usrname)
                                print (subprocess.Popen(cmd_ch,stdout=subprocess.PIPE,shell=True).communicate()[0])
elif (usrinput == "3"):
        usrname=raw_input("Enter the username\n")
        cmd_usr="last {0}".format(usrname)
        out_cmd_usr=subprocess.Popen(cmd_usr,stdout=subprocess.PIPE,shell=True).communicate()[0].split('\n')
        extra_usr=out_cmd_usr[0:-1]
        print ("Number of Times user {0} logged till now from date of installation is {1}".format(usrname,len(extra_usr)))
