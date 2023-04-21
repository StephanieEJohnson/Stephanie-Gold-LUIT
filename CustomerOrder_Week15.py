# Create a Standard SQS u=sing Python

import boto3

# SQS service resource
sqs =boto3.resource('sqs')

# Create SQS queue 
queue = sqs.create_queue(QueueName='Week15_project_LUIT')

print(queue.url)