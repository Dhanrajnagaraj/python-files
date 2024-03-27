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