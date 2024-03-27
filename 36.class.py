#!/usr/bin/python
import os
print (os.system("uptime;uname;free"))


#!/usr/bin/python
import subprocess
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

elif (usrinput == "4"):
        cmd_free="free"
        out_free=subprocess.Popen(cmd_free,stdout=subprocess.PIPE,shell=True).communicate()[0].split('\n')
        ramdetails=out_free[1]
        print ("Below are the Ram details of server\n{0}".format(ramdetails))
elif (usrinput == "5"):
        cmd_free="free"
        out_free=subprocess.Popen(cmd_free,stdout=subprocess.PIPE,shell=True).communicate()[0].split('\n')
        swapdetails=out_free[-2]
        print ("Below are swap details of server\n{0}".format(swapdetails))
