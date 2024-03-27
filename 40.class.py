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