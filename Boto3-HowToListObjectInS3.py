import boto3

s3_resource=boto3.client("s3")
objects=s3_resource.list_objects(Bucket="totaltechnology12181974") ["Contents"]
len(objects)
for object in objects:
    print(object["Key"])
    


