import boto3 
# how to upload single file

s3_resource=boto3.client('s3')
s3_resource.upload_file(
    Filename="./Stephanie-Gold-LUIT/Watermark.png",
    Bucket="totaltechnology12181974",
    Key="watermarktest.png")
    





    
    
