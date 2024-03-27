#####List of region 
#!/usr/bin/python
import boto3
ec2call=boto3.client('ec2',aws_access_key_id='AKIASOKOYD6SHCCXMBAG',aws_secret_access_key='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')
ec2_regions=ec2call.describe_regions()
ec2region=ec2_regions['Regions']
for j in range(0,len(ec2region),1):
    print (ec2region[j]['RegionName'])


#####list the region how many instance are available in user input vpcid state of the instance availaloty zone DNS 

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



################################################################
    
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




####instance list availability zone vpcid instance stopping and starting to user option


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