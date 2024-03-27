import boto3
#print (dir(boto3))
s3call=boto3.client('s3',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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',region_name='ap-south-1')




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





######ec2-service
        
#!/usr/bin/python
import boto3
ec2call=boto3.client('ec2',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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')
ec2_regions=ec2call.describe_regions()
ec2region=ec2_regions['Regions']
for j in range(0,len(ec2region),1):
    print (ec2region[j]['RegionName'])

#!/usr/bin/python
import boto3
ec2call=boto3.client('ec2')
#print (dir(ec2call))
list_re=ec2call.describe_regions()
region_out=list_re['Regions']
region_list=[]
for reg_ran in range(0,len(region_out),1):
    region_list.append(region_out[reg_ran]['RegionName'])
print (region_list)

usr_reg=raw_input("Enter the Required region name from above list\n")
print (usr_reg)

list_az=ec2call.describe_availability_zones()
azdetails=list_az['AvailabilityZones']
print ("Below are Availability zone under the region {0}\n".format(usr_reg))
for az_arn in range(0,len(azdetails),1):
    print (azdetails[az_arn]['ZoneName'])
    print (azdetails[az_arn]['ZoneId'])
    print ("=============================================")


ava_user_in=raw_input("Enter the availability zone from above list\n")

ec2details_fetching=ec2call.describe_instances()
instancedetails=ec2details_fetching['Reservations']
print (instancedetails)
for i in range(0,len(instancedetails),1):
#    print (instancedetails[0]['Instances'][0])

    dnsname=instancedetails[i]['Instances'][0]['PublicDnsName']
    state_of_instance=instancedetails[i]['Instances'][0]['State']['Name']
    private_ip_address=instancedetails[i]['Instances'][0]['PrivateIpAddress']
    vpcid=instancedetails[i]['Instances'][0]['VpcId']
    instanceid=instancedetails[i]['Instances'][0]['InstanceId']
    ava_zone=instancedetails[i]['Instances'][0]['Placement']['AvailabilityZone']
    print ("Below are details of instance {0}".format(instanceid))
    print (dnsname)
    print (state_of_instance)
    print (private_ip_address)
    print (vpcid)
    print (instanceid)
    print (ava_zone)
    print ("=======================================")





#!/usr/bin/python
import boto3
ec2call=boto3.client('ec2')
#print (dir(ec2call))
list_re=ec2call.describe_regions()
region_out=list_re['Regions']
region_list=[]
for reg_ran in range(0,len(region_out),1):
    region_list.append(region_out[reg_ran]['RegionName'])
print (region_list)

usr_reg=raw_input("Enter the Required region name from above list\n")
print (usr_reg)

list_az=ec2call.describe_availability_zones()
azdetails=list_az['AvailabilityZones']
print ("Below are Availability zone under the region {0}\n".format(usr_reg))
for az_arn in range(0,len(azdetails),1):
    print (azdetails[az_arn]['ZoneName'])
    print (azdetails[az_arn]['ZoneId'])
    print ("=============================================")


ava_user_in=raw_input("Enter the availability zone from above list\n")

ec2details_fetching=ec2call.describe_instances()
instancedetails=ec2details_fetching['Reservations']
print (instancedetails)
instanceid_details=[]
for i in range(0,len(instancedetails),1):
    #print (instancedetails[0]['Instances'][0])

    dnsname=instancedetails[i]['Instances'][0]['PublicDnsName']
    state_of_instance=instancedetails[i]['Instances'][0]['State']['Name']
    private_ip_address=instancedetails[i]['Instances'][0]['PrivateIpAddress']
    vpcid=instancedetails[i]['Instances'][0]['VpcId']
    instanceid=instancedetails[i]['Instances'][0]['InstanceId']
    ava_zone=instancedetails[i]['Instances'][0]['Placement']['AvailabilityZone']
    if (ava_zone == ava_user_in):
        print ("Below are details of instance {0} in Availability zone {1}".format(instanceid,ava_zone))
        print (dnsname)
        print (state_of_instance)
        print (private_ip_address)
        print (vpcid)
        print (instanceid)
        print (ava_zone)
        print ("=======================================")
        instanceid_details.append(instanceid)

print ("Below are Instance id in Availability zone {0}\n{1}".format(ava_user_in,instanceid_details))








#!/usr/bin/python
import boto3
ec2call=boto3.client('ec2')
#print (dir(ec2call))
list_re=ec2call.describe_regions()
region_out=list_re['Regions']
region_list=[]
for reg_ran in range(0,len(region_out),1):
    region_list.append(region_out[reg_ran]['RegionName'])
print (region_list)

usr_reg=raw_input("Enter the Required region name from above list\n")
print (usr_reg)

list_az=ec2call.describe_availability_zones()
azdetails=list_az['AvailabilityZones']
print ("Below are Availability zone under the region {0}\n".format(usr_reg))
for az_arn in range(0,len(azdetails),1):
    print (azdetails[az_arn]['ZoneName'])
    print (azdetails[az_arn]['ZoneId'])
    print ("=============================================")


ava_user_in=raw_input("Enter the availability zone from above list\n")

ec2details_fetching=ec2call.describe_instances()
instancedetails=ec2details_fetching['Reservations']
print (instancedetails)
instanceid_details=[]
for i in range(0,len(instancedetails),1):
    #print (instancedetails[0]['Instances'][0])

    dnsname=instancedetails[i]['Instances'][0]['PublicDnsName']
    state_of_instance=instancedetails[i]['Instances'][0]['State']['Name']
    private_ip_address=instancedetails[i]['Instances'][0]['PrivateIpAddress']
    vpcid=instancedetails[i]['Instances'][0]['VpcId']
    instanceid=instancedetails[i]['Instances'][0]['InstanceId']
    ava_zone=instancedetails[i]['Instances'][0]['Placement']['AvailabilityZone']
    if (ava_zone == ava_user_in):
        print ("Below are details of instance {0} in Availability zone {1}".format(instanceid,ava_zone))
        print (dnsname)
        print (state_of_instance)
        print (private_ip_address)
        print (vpcid)
        print (instanceid)
        print (ava_zone)
        print ("=======================================")
        instanceid_details.append(instanceid)

print ("Below are Instance id in Availability zone {0}\n{1}".format(ava_user_in,instanceid_details))

usrinput=raw_input("Enter '1' to start instances\n'2' to Stop instances\n'3' to start particular instanceid")
if (usrinput == "1"):
    print ("Now we are Start instances")
    ec2call_start=ec2call.start_instances(InstanceIds=instanceid_details)
    print (ec2call_start)
elif (usrinput == "2"):
    print ("Now we are stopping iinstances")
    ec2call_stop=ec2call.stop_instances(InstanceIds=instanceid_details)
    print (ec2call_stop)

elif (usrinput == "3"):
    par_ins=raw_input("Enter the Instance id from above list\n")
    ec2call_start_part=ec2call.start_instances(InstanceIds=[par_ins])
    print (ec2call_start_part)





#!/usr/bin/python
import boto3
ec2call=boto3.client('ec2')
#print (dir(ec2call))
list_re=ec2call.describe_regions()
region_out=list_re['Regions']
region_list=[]
for reg_ran in range(0,len(region_out),1):
    region_list.append(region_out[reg_ran]['RegionName'])
print (region_list)

usr_reg=raw_input("Enter the Required region name from above list\n")
print (usr_reg)

list_az=ec2call.describe_availability_zones()
azdetails=list_az['AvailabilityZones']
print ("Below are Availability zone under the region {0}\n".format(usr_reg))
for az_arn in range(0,len(azdetails),1):
    print (azdetails[az_arn]['ZoneName'])
    print (azdetails[az_arn]['ZoneId'])
    print ("=============================================")


ava_user_in=raw_input("Enter the availability zone from above list\n")

ec2details_fetching=ec2call.describe_instances()
instancedetails=ec2details_fetching['Reservations']
print (instancedetails)
instanceid_details=[]
for i in range(0,len(instancedetails),1):
    #print (instancedetails[0]['Instances'][0])

    dnsname=instancedetails[i]['Instances'][0]['PublicDnsName']
    state_of_instance=instancedetails[i]['Instances'][0]['State']['Name']
    private_ip_address=instancedetails[i]['Instances'][0]['PrivateIpAddress']
    vpcid=instancedetails[i]['Instances'][0]['VpcId']
    instanceid=instancedetails[i]['Instances'][0]['InstanceId']
    ava_zone=instancedetails[i]['Instances'][0]['Placement']['AvailabilityZone']
    if (ava_zone == ava_user_in):
        print ("Below are details of instance {0} in Availability zone {1}".format(instanceid,ava_zone))
        print (dnsname)
        print (state_of_instance)
        print (private_ip_address)
        print (vpcid)
        print (instanceid)
        print (ava_zone)
        print ("=======================================")
        instanceid_details.append(instanceid)

print ("Below are Instance id in Availability zone {0}\n{1}".format(ava_user_in,instanceid_details))

usrinput=raw_input("Enter '1' to start instances\n'2' to Stop instances\n'3' to start particular instanceid\n '4' to start All EC2 instance which are stopped mode")
if (usrinput == "1"):
    print ("Now we are Start instances")
    ec2call_start=ec2call.start_instances(InstanceIds=instanceid_details)
    print (ec2call_start)
elif (usrinput == "2"):
    print ("Now we are stopping iinstances")
    ec2call_stop=ec2call.stop_instances(InstanceIds=instanceid_details)
    print (ec2call_stop)

elif (usrinput == "3"):
    par_ins=raw_input("Enter the Instance id from above list\n")
    ec2call_start_part=ec2call.start_instances(InstanceIds=[par_ins])
    print (ec2call_start_part)

elif (usrinput == "4"):
    ec2details_fetching_status=ec2call.describe_instances(InstanceIds=instanceid_details)
    ec2_check_all=ec2details_fetching_status['Reservations']
    running_instances=[]
    stopped_instances=[]
    for j in range(0,len(ec2_check_all),1):
        print (ec2_check_all[j]['Instances'][0]['State']['Name'])
        print (ec2_check_all[j]['Instances'][0]['InstanceId'])
        instancesstate=ec2_check_all[j]['Instances'][0]['State']['Name']
        if (instancesstate == "running"):
            running_instances.append(ec2_check_all[j]['Instances'][0]['InstanceId'])
        elif (instancesstate == "stopped"):
            stopped_instances.append(ec2_check_all[j]['Instances'][0]['InstanceId'])
print ("Below are Running Instances\n{0}\nBelow are Stooped instances\n{1}".format(running_instances,stopped_instances))
opt=raw_input("Enter '1' to Stop the running instances\n'2' to start the stoopped instances")
if (opt == "1"):
    print ("Here we are Stopping running ec2 instances")
    ec2stop=ec2call.stop_instances(InstanceIds=running_instances)
elif (opt == "2"):
    print ("Here we are starting the stooped ec2 instances")
    ec2start=ec2call.start_instances(InstanceIds=stopped_instances)





#####security group service
    

#!/usr/bin/python
import boto3
ec2call=boto3.client('ec2')
sgcall=ec2call.describe_security_groups()
sgcall_out=sgcall['SecurityGroups']
for sg_ran in range(0,len(sgcall_out),1):
#    print (sgcall_out[sg_ran])
    print (sgcall_out[sg_ran].keys())
    print (sgcall_out[sg_ran]['GroupName'])
    print (sgcall_out[sg_ran]['VpcId'])
    print (sgcall_out[sg_ran]['GroupId'])
    print (sgcall_out[sg_ran]['IpPermissions'][0])
    try:
        print (sgcall_out[sg_ran]['IpPermissions'][0]['FromPort'])
        print (sgcall_out[sg_ran]['IpPermissions'][0]['ToPort'])
    except:
        pass
    print ("=======================================")




#!/usr/bin/python
import boto3
finaldetails=[]
ec2call=boto3.client('ec2')
ebs_descr=ec2call.describe_volumes()
#print (ebs_descr)
ebsvolumedetails=ebs_descr['Volumes']
#print (len(ebsvolumedetails))
for ebs_ran in range(0,len(ebsvolumedetails),1):
    details={}
#    print (ebsvolumedetails[ebs_ran].keys())
    avaz=ebsvolumedetails[ebs_ran]['AvailabilityZone']
    volid=ebsvolumedetails[ebs_ran]['VolumeId']
    volst=ebsvolumedetails[ebs_ran]['State']
    details['availzone']=avaz
    details['volumeid']=volid
    details['state']=volst
#    print (details)
    finaldetails.append(details)
#    print ("======================================================")

print (finaldetails)

usr_avaz=raw_input("Enter the availability zone\n")
volume_id_ava=[]
for gh in range(0,len(finaldetails),1):
    if (finaldetails[gh]['availzone'] == usr_avaz) and (finaldetails[gh]['state'] == "available"):
        volume_id_ava.append(finaldetails[gh]['volumeid'])


print ("Fetching ec2 instance details under {0}".format(usr_avaz))
ec2instance=ec2call.describe_instances()
details_instance=ec2instance['Reservations']
instance_id=[]
for ece_ran in range(0,len(details_instance),1):
#    print (details_instance[ece_ran]['Instances'][0]['InstanceId'])
    avaz_op=details_instance[ece_ran]['Instances'][0]['Placement']['AvailabilityZone']
    if (avaz_op == usr_avaz):
        instance_id.append(details_instance[ece_ran]['Instances'][0]['InstanceId'])
print ("Below are Instance under {0}\n{1}".format(usr_avaz,instance_id))
print ("Below are Volume id which are free under {0}\n{1}".format(usr_avaz,volume_id_ava))
usr_instan=raw_input("Enter the Instance from Above list\n")
vol_idd=raw_input("Enter the Volume id from above list\n")
attaching_volume=ec2call.attach_volume(Device='/dev/xvdf',InstanceId=usr_instan,VolumeId=vol_idd)
print (attaching_volume)




###EC2 INSTANCE CREATION

!/usr/bin/python
import boto3
ec2_call_region=boto3.client('ec2')
def regioncollection():
    global regionlist
    regionlist=[]
    region_collections=ec2_call_region.describe_regions()
    for regid in range(0,len(region_collections['Regions']),1):
        if region_collections['Regions'][regid]['RegionName'].strip() not in  regionlist:
            regionlist.append(region_collections['Regions'][regid]['RegionName'].strip())
    print( "Below are Regions available in aws account \n\n\n {0}".format("\n".join(regionlist)))

regioncollection()



regionname_input=raw_input("Enter the Region name required from above list\n")

ec2_call=boto3.client('ec2','{0}'.format(regionname_input))

def collectingkeypairs():
    keypair_collection=[]
    keypaircollection=ec2_call.describe_key_pairs()
    for keypaircoll in range(0,len(keypaircollection['KeyPairs']),1):
        if keypaircollection['KeyPairs'][keypaircoll]['KeyName'] not in keypair_collection:
            keypair_collection.append(keypaircollection['KeyPairs'][keypaircoll]['KeyName'])
    print( "Below are the Key pair collection in the region {0}\n\n\n{1}".format(regionname_input.strip(),"\n".join(keypair_collection))        )


collectingkeypairs()    
#print( dir(ec2_call))
#print( dir(ec2_call.run_instances()))

aws_key_pair=raw_input("Enter the key pair from above list\n")
print (aws_key_pair)

def collecting_security_groups():
    global security_group_list
    global security_group_collection
    security_group_list=[]
    security_group_collection=ec2_call.describe_security_groups()
    for sec in range(0,len(security_group_collection['SecurityGroups']),1):
        if security_group_collection['SecurityGroups'][sec]['GroupName'] not in security_group_list:
            security_group_list.append(security_group_collection['SecurityGroups'][sec]['GroupName'])
#    print( "\nBelow are the Security group available in the region  {0}\n\n{1}".format(regionname_input.strip(),"\n".join(security_group_list))        )


collecting_security_groups()   




def collecting_subnet_details():
    global subnet_list
    global subnet_collections
    subnet_list=[]

    subnet_collections=ec2_call.describe_subnets()
    for subran in range(0,len(subnet_collections['Subnets']),1):
        if  subnet_collections['Subnets'][subran]['SubnetId'] not in subnet_list:
            subnet_list.append(subnet_collections['Subnets'][subran]['SubnetId'])
#    print( "\n Below are the Subnets available in the region {0}\n\n{1}".format(regionname_input.strip(),"\n".join(subnet_list)))



collecting_subnet_details()   


count_instances_required=raw_input("Enter the count of instances required\n")
print( "Below are the Regions available in aws account\n\n{0}\n".format("\n".join(regionlist)))
regionselect=raw_input("Enter Any one region name where you want to create instances\n")
print( regionselect)

print( "Below are Subnets available available in  the region {0}\n\n{1}".format(regionselect.strip(),"\n".join(subnet_list)))

subnetselect=raw_input("Enter Any one subnet name from above list which will be used to create EC2 instance\n\n")

print( subnetselect)

def selected_subnet_details():
    global vpcid_selected 
    for selesubn in range(0,len(subnet_collections['Subnets']),1):
        if(subnet_collections['Subnets'][selesubn]['SubnetId'] == str(subnetselect.strip())):
            print( "Below are the details of Subnet {0} in region {1}\n\n".format(subnetselect.strip(),regionselect.strip()))
            print( "PublicIp_on_launch: {0}".format( subnet_collections['Subnets'][selesubn]['MapPublicIpOnLaunch']))
            print( "Vpc_id: {0}".format(subnet_collections['Subnets'][selesubn]['VpcId']))
            vpcid_selected="{0}".format(subnet_collections['Subnets'][selesubn]['VpcId'])
            print( "Available_IP_adress_count: {0}".format(subnet_collections['Subnets'][selesubn]['AvailableIpAddressCount']))
            print( "CIDR_Block_range: {0}".format(subnet_collections['Subnets'][selesubn]['CidrBlock']))
            print( "Subnet_state: {0}".format(subnet_collections['Subnets'][selesubn]['State']))
            print( "Availability_zone: {0}\n\n".format(subnet_collections['Subnets'][selesubn]['AvailabilityZone']))

selected_subnet_details()    

#print( "Below are the Security Group details available in the region {0}\n\n{1}".format(regionselect.strip(),"\n".join(security_group_list)))

#selectsecuritygrp=raw_input("Enter the Security group from above list which will be used to create EC2 instance\n\n")

def security_group_collection_collect():
    security_group_under_vpcids=[]
#    print( security_group_collection['SecurityGroups'])
    for secran in range(0,len(security_group_collection['SecurityGroups']),1):
        if (security_group_collection['SecurityGroups'][secran]['VpcId'] == str(vpcid_selected)):
            if security_group_collection['SecurityGroups'][secran]['GroupName'] not in security_group_under_vpcids:
                security_group_under_vpcids.append(security_group_collection['SecurityGroups'][secran]['GroupName'])
    if(len(security_group_under_vpcids)>0):            
        print( "Below are the security Groups available  under Vpcid {0}\n\n{1}".format(vpcid_selected,"\n".join(security_group_under_vpcids)))


security_group_collection_collect()


selectsecuritygrp=raw_input("Enter the Security group from above list which will be used to create EC2 instance\n\n")
print( selectsecuritygrp)

def Collecting_details_selected_security_group():
    global selectsecuritygrp
    Inbound_port=[]
    Outbound_port=[]
    for selecsg_range in range(0,len(security_group_collection['SecurityGroups']),1):
        if (str(security_group_collection['SecurityGroups'][selecsg_range]['GroupName']) == str(selectsecuritygrp)):
            print( security_group_collection['SecurityGroups'][selecsg_range]['GroupName'])
            print( "\n\nBelow are the Details of security group {0}\n\n".format(selectsecuritygrp.strip()))
            #print( security_group_collection['SecurityGroups'][selecsg_range])
            print( "Security_Group_id: {0}".format(security_group_collection['SecurityGroups'][selecsg_range]['GroupId']))
            selectsecuritygrp="{0}".format(security_group_collection['SecurityGroups'][selecsg_range]['GroupId'])
            print( "Vpc_id: {0}".format(security_group_collection['SecurityGroups'][selecsg_range]['VpcId']))
            for inbound in range(0,len(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions']),1):
                if security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][inbound]['ToPort'] not in Inbound_port:
                    Inbound_port.append(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][inbound]['ToPort'])    
            for oubound in range(0,len(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions']),1):
                if security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][oubound]['FromPort'] not in Outbound_port:
                    Outbound_port.append(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][oubound]['FromPort'])
            print( "Inbound_Port details: {0}".format(Inbound_port))
            print( "Outbound_Port_details: {0}".format(Outbound_port))

      



Collecting_details_selected_security_group()            




instance_type=raw_input("Enter the Instance type\n")
ami_id=raw_input("Enter the ami id\n")


#def creating_instances():
#    instance_creation=ec2_call.run_instances(ImageId="ami-0c6615d1e95c98aca",InstanceType="{0}".format(instance_type.strip()),KeyName="{0}".format('nov15'),MaxCount=int(count_instances_required),MinCount=int(1),SecurityGroupIds=[selectsecuritygrp],SubnetId="{0}".format(subnetselect.strip()),NetworkInterfaces=[
#    {
#        'DeviceIndex': 0,
#        'SubnetId' : subnetselect.strip(),
#        'Groups': [selectsecuritygrp],
#        ]
#        'AssociatePublicIpAddress': True            
#    })
#    print( instance_creation)


#creating_instances()

#kj=ec2_call.run_instances(InstanceType=str(instance_type.strip()),
#                         MaxCount=int(count_instances_required),
#                         MinCount=int(count_instances_required),
#                         ImageId="ami-0c6615d1e95c98aca")

#print( kj)

ec2_call_create=boto3.resource('ec2',region_name='{0}'.format(regionname_input))

def creating_instances():
    global instance_creation
    instance_creation=ec2_call_create.create_instances(ImageId="{0}".format(ami_id),InstanceType="{0}".format(instance_type.strip()),KeyName="{0}".format(aws_key_pair),MaxCount=int(count_instances_required),MinCount=int(1),NetworkInterfaces=[
    {
        'DeviceIndex': 0,
        'SubnetId' : subnetselect.strip(),
        'Groups': [selectsecuritygrp],
        
        'AssociatePublicIpAddress': True
    }])
#    print( dir(instance_creation))
#    instance_creation.reload()

    for instanceid in instance_creation:
        print( instanceid.id)
        instanceid.wait_until_running()




creating_instances()    



def Fetching_details_instances():
    for insdeta in instance_creation:
        instance_id_de=insdeta.id
        desinsta=ec2_call.describe_instances(InstanceIds=[instance_id_de])
        print( "\n\nBelow are the details of Newly created instance id {0}\n\n".format(instance_id_de))
        print( "Public_DNS_NAME: {0}".format(desinsta['Reservations'][0]['Instances'][0]['PublicDnsName']))
        print( "State of instance: {0}".format(desinsta['Reservations'][0]['Instances'][0]['State']['Name']))
        print( "Public_IP_Adress: {0}".format(desinsta['Reservations'][0]['Instances'][0]['PublicIpAddress']))
        print( "Vpc_id: {0}".format(desinsta['Reservations'][0]['Instances'][0]['VpcId'] ))
        print( "Cpu_core_details: {0}".format(desinsta['Reservations'][0]['Instances'][0]['CpuOptions']['CoreCount']))
        print( "Image-id_of_instance: {0}".format(desinsta['Reservations'][0]['Instances'][0]['ImageId']))
        print( "Private_IP_Adress: {0}".format(desinsta['Reservations'][0]['Instances'][0]['PrivateIpAddress']))
        print( "Keypairname: {0}".format(desinsta['Reservations'][0]['Instances'][0]['KeyName']))
        print( "Security_groups: {0}".format(desinsta['Reservations'][0]['Instances'][0]['SecurityGroups']))
        print( "Subnet_id: {0}".format(desinsta['Reservations'][0]['Instances'][0]['SubnetId']))
        print( "root_device_name: {0}".format(desinsta['Reservations'][0]['Instances'][0]['RootDeviceName']))
        print( "root_device_type: {0}".format(desinsta['Reservations'][0]['Instances'][0]['RootDeviceType']))
        print( "\n\n===============End of details of instance id {0}======================================\n\n".format(instance_id_de))



Fetching_details_instances()