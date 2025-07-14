# Importing the boto3 library
import boto3

ec2 = boto3.resource('ec2')
instance_name = 'dct-ec2-instance'

#Store instance ID
instance_id = None

#Create a list of all instances that we have
instances = ec2.instances.all()
instances_exists = False

for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instances_exists = True
            instance_id = instance.id
            print(f"An instance named {instance_name} with ID {instance_id} already exists.")
            break
    if instances_exists:
        break

#Launch a new EC2 instance
if not instances_exists:
    new_instance = ec2.create_instances(
        ImageId = 'ami-0d03cb826412c6b0f',
        MinCount = 1,
        MaxCount = 1,
        InstanceType = 't2.micro',
    KeyName='test-key-pair',
    TagSpecifications = [
        {
            'ResourceType': 'instance',
            'Tags':[
                {
                    "Key": 'Name',
                    "Value": f'{instance_name}'
                },
            ]
        },
    ]

)
    instance_id = new_instance[0].id
    print(f"Created a new instance named {instance_name} with ID {instance_id}.")

# #Stop the instance 
# ec2.Instance(instance_id).stop()

# #Start the instance
# ec2.Instance(instance_id).start()

#Terminate the instance
# ec2.Instance(instance_id).terminate()

