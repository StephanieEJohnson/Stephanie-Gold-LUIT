# Create a list of AWS Services 

# Create a empty list
list_services = [0]

# Populate a list of AWS Services using append
list_services.append('S3')
list_services.append('EC2')
list_services.append('DynamoDB')
list_services.append('ECS')
list_services.append('Lambda')

# Print AWS Service list and the lenght of the list
print(list_services)
print(len(list_services))

# Remove two specific services from the list by name 
list_services.remove("S3")
list_services.remove("Lambda")
print(list_services)

# Print new AWS Service list with lenght of the list
print(len(list_services))



