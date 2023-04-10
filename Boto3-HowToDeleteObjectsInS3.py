import boto3
# delete single object  
s3_resource=boto3.client("s3")
s3_resource.delete_object(Bucket='totaltechnology12181974',
    Key='3 Tier .png')
    
    
#delete multiple objects  
import os
import glob

# find all the objects from the s3 bucket
objects=s3_resource.list_objects(Bucket="totaltechnology12181974")["Contents"]
len(objects)

# iteration
for object in objects:
       s3_resource.delete_object(Bucket='totaltechnology12181974',
        Key=object["Key"])
        
        