# Stopping Running EC2 instance using phython

import boto3

client = boto3.client('ec2')
# this will start ec2 instance with Filter using tag name

'''tag_Project_Instance={'Name': 'tag:Project_Instance', 'Values':['Yes']}
for each_ins in client.describe_instances(Filters=[tag_Project_Instance])['Reservations']:
    for inst_id in each_ins['Instances']:
        #print (inst_id['InstanceId'])
       # client.start_instances(InstanceIds=[inst_id['InstanceId']])'''

#This will stop all running EC2 instances        
tag_Project_Instance={'Name': 'tag:Project_Instance', 'Values':['Yes']}
for each_ins in client.describe_instances(Filters=[tag_Project_Instance])['Reservations']:
    for inst_id in each_ins['Instances']:
        #print (inst_id['InstanceId'])
        client.stop_instances(InstanceIds=[inst_id['InstanceId']])    
        
        
        
        
        
        
        
        
        
        
        

      
      
      
      
      
      
        
        
        
        
        




    
    

 



 

