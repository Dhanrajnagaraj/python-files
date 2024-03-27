####Simple storage service
AWS credentiall access
import boto3
#print (dir(boto3))
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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',region_name='ap-south-1')


###########S3 Bucket list

import boto3
#print (dir(boto3))
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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',region_name='ap-south-1')
#print (dir(s3call))

list_buckets=s3call.list_buckets()
print (list_buckets)

import boto3
#print (dir(boto3))
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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',region_name='ap-south-1')
#print (dir(s3call))
bucket_exsists=[]
list_buckets=s3call.list_buckets()
#print (list_buckets)
bucketlist=list_buckets['Buckets']
#print (bucketlist)
count_of_buck=len(bucketlist)
for i in range(0,count_of_buck,1):
    #print (bucketlist[i]['Name'])
    bucket_exsists.append(bucketlist[i]['Name'])
print ("Below are Buckets Available in Account\n{0}".format("\n".join(bucket_exsists)))


### bucket name with number 
import boto3
import re
alphmatch=re.compile(r'^[a-z]+$')
numbermatch=re.compile(r'[0-9]+$')
#print (dir(boto3))
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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',region_name='ap-south-1')
#print (dir(s3call))
bucket_exsists=[]
list_buckets=s3call.list_buckets()
#print (list_buckets)
bucketlist=list_buckets['Buckets']
#print (bucketlist)
count_of_buck=len(bucketlist)
for i in range(0,count_of_buck,1):
    #print (bucketlist[i]['Name'])
    bucket_exsists.append(bucketlist[i]['Name'])
#print ("Below are Buckets Available in Account\n{0}".format("\n".join(bucket_exsists)))

if (count_of_buck < 3):
    print ("Count of buckets available is {0}".format(count_of_buck))
else:
    print ("Below are Buckets available in account\n{0}".format("\n".join(bucket_exsists)))
    userinput=input("Enter '1' to display alphabet bucket\n'2' to display numerical bucket\n")
    if (userinput == "1"):
        for buckename in bucket_exsists:
            if re.search(alphmatch,buckename):
                print ("Bucket {0} contains  only alphabet".format(buckename))
    elif (userinput == "2"):
        for buckename in bucket_exsists:
            if re.search(numbermatch,buckename):
                print ("Bucket {0} contains  only alphabet".format(buckename))



#####S3 bucket alphanumaric name list
                
import boto3
import re
alphmatch=re.compile(r'^[a-z]+$')
numbermatch=re.compile(r'[0-9]+$')
alphamatch_1=re.compile(r'[a-z]')
numbermatch_1=re.compile(r'[0-9]')
#print (dir(boto3))
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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')
#print (dir(s3call))
bucket_exsists=[]
list_buckets=s3call.list_buckets()
#print (list_buckets)
bucketlist=list_buckets['Buckets']
#print (bucketlist)
count_of_buck=len(bucketlist)
for i in range(0,count_of_buck,1):
    #print (bucketlist[i]['Name'])
    bucket_exsists.append(bucketlist[i]['Name'])
#print ("Below are Buckets Available in Account\n{0}".format("\n".join(bucket_exsists)))

if (count_of_buck < 3):
    print ("Count of buckets available is {0}".format(count_of_buck))
else:
    print ("Below are Buckets available in account\n{0}".format("\n".join(bucket_exsists)))
    userinput=input("Enter '1' to display alphabet bucket\n'2' to display numerical bucket\n'3' to list buckets which contains alphabet and number")
    if (userinput == "1"):
        for buckename in bucket_exsists:
            if re.search(alphmatch,buckename):
                print ("Bucket {0} contains  only alphabet".format(buckename))
    elif (userinput == "2"):
        for buckename in bucket_exsists:
            if re.search(numbermatch,buckename):
                print ("Bucket {0} contains  only alphabet".format(buckename))
    elif (userinput == "3"):
        for buckename in bucket_exsists:
            if re.search(numbermatch_1,buckename) and re.search(alphamatch_1,buckename):
                print ("Bucket {0} contains both alphabet and number".format(buckename))



###name and size of the bucket and inside the bucket objet is present or nut checking
import boto3
bucketexsists=[]
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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')
#print (dir(s3call))
bucketlist=s3call.list_buckets()
bucketdetails=bucketlist['Buckets']
count_of_bucke=len(bucketlist['Buckets'])
for buc_ran in range(0,count_of_bucke,1):
    #print (bucketdetails[buc_ran]['Name'])
    bucketexsists.append(bucketdetails[buc_ran]['Name'])

print ("Below are Buckets Available in account\n{0}".format('\n'.join(bucketexsists)))
usr_inp_bucke=input("Enter the Bucket to be checked\n")
if (usr_inp_bucke in bucketexsists):
    print ("Bucket {0} exsists".format(usr_inp_bucke))
else:
    print ("Bucket {0} doesnt exsists".format(usr_inp_bucke))



import boto3
bucketexsists=[]
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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')
#print (dir(s3call))
bucketlist=s3call.list_buckets()
bucketdetails=bucketlist['Buckets']
count_of_bucke=len(bucketlist['Buckets'])
for buc_ran in range(0,count_of_bucke,1):
    #print (bucketdetails[buc_ran]['Name'])
    bucketexsists.append(bucketdetails[buc_ran]['Name'])

print ("Below are Buckets Available in account\n{0}".format('\n'.join(bucketexsists)))
usr_inp_bucke=input("Enter the Bucket to be checked\n")
if (usr_inp_bucke in bucketexsists):
    print ("Bucket {0} exsists".format(usr_inp_bucke))
    s3objectall=s3call.list_objects(Bucket=usr_inp_bucke)
    #print (s3objectall.keys())
    s3objectlist=s3objectall['Contents']
    count_of_object=len(s3objectlist)
    for obj_ran in range(0,count_of_object,1):
        name_of_objec=s3objectlist[obj_ran]['Key']
        size_of_object=s3objectlist[obj_ran]['Size']
        print ("Below are details of Object {0} in Bucket {1}\nname={0}\nsize={2}\n================".format(name_of_objec,usr_inp_bucke,size_of_object))
else:
    print ("Bucket {0} doesnt exsists".format(usr_inp_bucke))

####bucket how many bucket available in server and object is present or not

import boto3
bucketexsists=[]
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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')
#print (dir(s3call))
bucketlist=s3call.list_buckets()
bucketdetails=bucketlist['Buckets']
count_of_bucke=len(bucketlist['Buckets'])
for buc_ran in range(0,count_of_bucke,1):
    #print (bucketdetails[buc_ran]['Name'])
    bucketexsists.append(bucketdetails[buc_ran]['Name'])

print ("Below are Buckets Available in account\n{0}".format('\n'.join(bucketexsists)))
usr_inp_bucke=input("Enter the Bucket to be checked\n")
if (usr_inp_bucke in bucketexsists):
    print ("Bucket {0} exsists".format(usr_inp_bucke))
    s3objectall=s3call.list_objects(Bucket=usr_inp_bucke)
    print (s3objectall)
    #print (s3objectall.keys())
    if "Contents" in s3objectall:
        s3objectlist=s3objectall['Contents']
        count_of_object=len(s3objectlist)
        for obj_ran in range(0,count_of_object,1):
            name_of_objec=s3objectlist[obj_ran]['Key']
            size_of_object=s3objectlist[obj_ran]['Size']
            print ("Below are details of Object {0} in Bucket {1}\nname={0}\nsize={2}\n================".format(name_of_objec,usr_inp_bucke,size_of_object))
    else:
        print ("No objecs available in bucket {0} and its empty bucket".format(usr_inp_bucke))
else:
    print ("Bucket {0} doesnt exsists".format(usr_inp_bucke))



###Number of object are present in the bucket
    
import boto3
bucketexsists=[]
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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',region_name='ap-south-1')
#print (dir(s3call))
bucketlist=s3call.list_buckets()
bucketdetails=bucketlist['Buckets']
count_of_bucke=len(bucketlist['Buckets'])
for buc_ran in range(0,count_of_bucke,1):
    #print (bucketdetails[buc_ran]['Name'])
    bucketexsists.append(bucketdetails[buc_ran]['Name'])

print ("Below are Buckets Available in account\n{0}".format('\n'.join(bucketexsists)))
usr_inp_bucke=input("Enter the Bucket to be checked\n")
if (usr_inp_bucke in bucketexsists):
    print ("Bucket {0} exsists".format(usr_inp_bucke))
    s3objectall=s3call.list_objects(Bucket=usr_inp_bucke)
    print (s3objectall)
    #print (s3objectall.keys())
    if 'Contents' in s3objectall:
        s3objectlist=s3objectall['Contents']
        count_of_object=len(s3objectlist)
        for obj_ran in range(0,count_of_object,1):
            name_of_objec=s3objectlist[obj_ran]['Key']
            size_of_object=s3objectlist[obj_ran]['Size']
            print ("Below are details of Object {0} in Bucket {1}\nname={0}\nsize={2}\n================".format(name_of_objec,usr_inp_bucke,size_of_object))
    else:
        print ("No objecs available in bucket {0} and its empty bucket".format(usr_inp_bucke))
else:
    print ("Bucket {0} doesnt exsists".format(usr_inp_bucke))
    usr_conf=input("Enter 'yes' to create bucket")
    if (usr_conf == "yes"):
        bucket_exsiting_post_crea=[]
        print ("User confirmed to create Bucket {0}".format(usr_inp_bucke))
        location_buck=input("Enter the location where bucket need to be created")
        cre_buk=s3call.create_bucket(Bucket=usr_inp_bucke,CreateBucketConfiguration={'LocationConstraint':location_buck})
        print (cre_buk)
        list_bu_pos_crea=s3call.list_buckets()
        bucket_listing=list_bu_pos_crea['Buckets']
        for jk in bucket_listing:
            bucket_exsiting_post_crea.append(jk['Name'])
        if (usr_inp_bucke in bucket_exsiting_post_crea):
            print ("Bucket {0} successfully created post user confirmation".format(usr_inp_bucke))
        else:
            print ("Bucket {0} not created due to permission issue or parameter".format(usr_inp_bucke))

    else:
        print ("User Not confirmed to create Bucket {0}".format(usr_inp_bucke))



###bucket checking if not present in the bucket user confirm to create a bucket in specifis region

import boto3
bucketexsists=[]
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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',region_name='ap-south-1')
#print (dir(s3call))
bucketlist=s3call.list_buckets()
bucketdetails=bucketlist['Buckets']
count_of_bucke=len(bucketlist['Buckets'])
for buc_ran in range(0,count_of_bucke,1):
    #print (bucketdetails[buc_ran]['Name'])
    bucketexsists.append(bucketdetails[buc_ran]['Name'])

print ("Below are Buckets Available in account\n{0}".format('\n'.join(bucketexsists)))
usr_inp_bucke=input("Enter the Bucket to be checked\n")
if (usr_inp_bucke in bucketexsists):
    print ("Bucket {0} exsists".format(usr_inp_bucke))
    s3objectall=s3call.list_objects(Bucket=usr_inp_bucke)
    print (s3objectall)
    #print (s3objectall.keys())
    if 'Contents' in s3objectall:
        s3objectlist=s3objectall['Contents']
        count_of_object=len(s3objectlist)
        for obj_ran in range(0,count_of_object,1):
            name_of_objec=s3objectlist[obj_ran]['Key']
            size_of_object=s3objectlist[obj_ran]['Size']
            print ("Below are details of Object {0} in Bucket {1}\nname={0}\nsize={2}\n================".format(name_of_objec,usr_inp_bucke,size_of_object))
    else:
        print ("No objecs available in bucket {0} and its empty bucket".format(usr_inp_bucke))
else:
    print ("Bucket {0} doesnt exsists".format(usr_inp_bucke))
    usr_conf=input("Enter 'yes' to create bucket")
    if (usr_conf == "yes"):
        bucket_exsiting_post_crea=[]
        print ("User confirmed to create Bucket {0}".format(usr_inp_bucke))
        location_buck=input("Enter the location where bucket need to be created")
        cre_buk=s3call.create_bucket(Bucket=usr_inp_bucke,CreateBucketConfiguration={'LocationConstraint':location_buck})
        print (cre_buk)
        list_bu_pos_crea=s3call.list_buckets()
        bucket_listing=list_bu_pos_crea['Buckets']
        for jk in bucket_listing:
            bucket_exsiting_post_crea.append(jk['Name'])
        if (usr_inp_bucke in bucket_exsiting_post_crea):
            print ("Bucket {0} successfully created post user confirmation".format(usr_inp_bucke))
        else:
            print ("Bucket {0} not created due to permission issue or parameter".format(usr_inp_bucke))

    else:
        print ("User Not confirmed to create Bucket {0}".format(usr_inp_bucke))

s3bucket_list_final=s3call.list_buckets()
bucketdetails_final=s3bucket_list_final['Buckets']
print ("Below are Buckets Available in account")
for j in range(0,len(bucketdetails_final),1):
    print (bucketdetails_final[j]['Name'])
usrop=input("Enter '1' to upload object\n'2' to download object\n'3' to delete object")
if (usrop == "1"):
    objelist=[]
    buck=input("Enter the Bucketname to upliad\n")
    s3file=input("Enter the s3 filename\n")
    localfilename=input("Enter the localfilenamepath\n")
    uploadoperation=s3call.upload_file(localfilename,buck,s3file)
    s3list_objects=s3call.list_objects(Bucket=buck)
    list_objects=s3list_objects['Contents']
    for obj_ran in range(0,len(list_objects),1):
        objelist.append(list_objects[obj_ran]['Key'])
    if s3file in objelist:
        print ("{0} file uploaded successfully in bucket {1}".format(s3file,buck))


####bucket checking creat a bucket and check the how many object/file present in the bucket add the object to particular bucket user option
        
import boto3
bucketexsists=[]
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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',region_name='ap-south-1')
#print (dir(s3call))
bucketlist=s3call.list_buckets()
bucketdetails=bucketlist['Buckets']
count_of_bucke=len(bucketlist['Buckets'])
for buc_ran in range(0,count_of_bucke,1):
    #print (bucketdetails[buc_ran]['Name'])
    bucketexsists.append(bucketdetails[buc_ran]['Name'])

print ("Below are Buckets Available in account\n{0}".format('\n'.join(bucketexsists)))
usr_inp_bucke=input("Enter the Bucket to be checked\n")
if (usr_inp_bucke in bucketexsists):
    print ("Bucket {0} exsists".format(usr_inp_bucke))
    s3objectall=s3call.list_objects(Bucket=usr_inp_bucke)
    print (s3objectall)
    #print (s3objectall.keys())
    if 'Contents' in s3objectall:
        s3objectlist=s3objectall['Contents']
        count_of_object=len(s3objectlist)
        for obj_ran in range(0,count_of_object,1):
            name_of_objec=s3objectlist[obj_ran]['Key']
            size_of_object=s3objectlist[obj_ran]['Size']
            print ("Below are details of Object {0} in Bucket {1}\nname={0}\nsize={2}\n================".format(name_of_objec,usr_inp_bucke,size_of_object))
    else:
        print ("No objecs available in bucket {0} and its empty bucket".format(usr_inp_bucke))
else:
    print ("Bucket {0} doesnt exsists".format(usr_inp_bucke))
    usr_conf=input("Enter 'yes' to create bucket")
    if (usr_conf == "yes"):
        bucket_exsiting_post_crea=[]
        print ("User confirmed to create Bucket {0}".format(usr_inp_bucke))
        location_buck=input("Enter the location where bucket need to be created")
        cre_buk=s3call.create_bucket(Bucket=usr_inp_bucke,CreateBucketConfiguration={'LocationConstraint':location_buck})
        print (cre_buk)
        list_bu_pos_crea=s3call.list_buckets()
        bucket_listing=list_bu_pos_crea['Buckets']
        for jk in bucket_listing:
            bucket_exsiting_post_crea.append(jk['Name'])
        if (usr_inp_bucke in bucket_exsiting_post_crea):
            print ("Bucket {0} successfully created post user confirmation".format(usr_inp_bucke))
        else:
            print ("Bucket {0} not created due to permission issue or parameter".format(usr_inp_bucke))

    else:
        print ("User Not confirmed to create Bucket {0}".format(usr_inp_bucke))

s3bucket_list_final=s3call.list_buckets()
bucketdetails_final=s3bucket_list_final['Buckets']
print ("Below are Buckets Available in account")
for j in range(0,len(bucketdetails_final),1):
    print (bucketdetails_final[j]['Name'])
usrop=input("Enter '1' to upload object\n'2' to download object\n'3' to delete object")
if (usrop == "1"):
    objelist=[]
    buck=input("Enter the Bucketname to upliad\n")
    s3file=input("Enter the s3 filename\n")
    localfilename=input("Enter the localfilenamepath\n")
    uploadoperation=s3call.upload_file(localfilename,buck,s3file)
    s3list_objects=s3call.list_objects(Bucket=buck)
    list_objects=s3list_objects['Contents']
    for obj_ran in range(0,len(list_objects),1):
        objelist.append(list_objects[obj_ran]['Key'])
    if s3file in objelist:
        print ("{0} file uploaded successfully in bucket {1}".format(s3file,buck))

elif (usrop == "2"):
    buck = input("Enter the Bucketname from where we need to download\n")
    s3list_objects = s3call.list_objects(Bucket=buck)
    objectlisting=s3list_objects['Contents']
    print ("Below are Objects are available in Bucket {0}".format(buck))
    for o in range(0,len(objectlisting),1):
        print (objectlisting[o]['Key'])
    s3filename=input("Enter the filename from above list which need to be downlaoded")
    localfilenamepath=input("Enter the local path  of file to be download")
    with open(localfilenamepath,'wb') as lb:
        s3call.download_fileobj(buck, s3filename, lb)