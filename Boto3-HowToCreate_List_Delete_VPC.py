# How to create VPC using python

import boto3

client=boto3.client("ec2")
client.create_vpc(CidrBlock='10.0.0.0/16')

# How to list VPCs using python
import boto3


vpc = boto3.client('ec2')

response = vpc.describe_vpcs()

vpcs = response['Vpcs']

for vpc in vpcs:
    print(vpc['VpcId'])
    
# How to delete VPC using python

import boto3

client=boto3.client('ec2')
response =client.delete_vpc(
    VpcId='vpc-093927b9f5e07dfe4'
)












