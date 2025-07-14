import boto3
import time

ec2 = boto3.client('ec2')

vpc_name = 'vpc-sumukha'
ig_name = 'ig-vpc-sumukha'

# Fetch VPC ID by Name tag
vpcs = ec2.describe_vpcs(
    Filters=[{'Name': 'tag:Name', 'Values': [vpc_name]}]
    )['Vpcs']
if not vpcs:
    print("No matching VPC found.")
    exit()

vpc_id = vpcs[0]['VpcId']
print(f"Found VPC: {vpc_id}")

# Get and delete EC2 instances in the VPC (if any)
instances = ec2.describe_instances(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
for res in instances['Reservations']:
    for instance in res['Instances']:
        instance_id = instance['InstanceId']
        print(f"Terminating EC2 instance: {instance_id}")
        ec2.terminate_instances(InstanceIds=[instance_id])
        ec2.get_waiter('instance_terminated').wait(InstanceIds=[instance_id])
        print(f"Terminated: {instance_id}")

# Detach and delete Internet Gateway
igws = ec2.describe_internet_gateways(Filters=[{'Name': 'tag:Name', 'Values': [ig_name]}])['InternetGateways']
if igws:
    ig_id = igws[0]['InternetGatewayId']
    print(f"Detaching and deleting IGW: {ig_id}")
    ec2.detach_internet_gateway(InternetGatewayId=ig_id, VpcId=vpc_id)
    ec2.delete_internet_gateway(InternetGatewayId=ig_id)

# Delete route tables (skip main route table)
route_tables = ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])['RouteTables']
for rt in route_tables:
    main_association = any(assoc.get('Main', False) for assoc in rt['Associations'])
    if main_association:
        continue
    rt_id = rt['RouteTableId']
    
    # Disassociate from subnets
    for assoc in rt['Associations']:
        if not assoc.get('Main'):
            assoc_id = assoc['RouteTableAssociationId']
            print(f"Disassociating route table {rt_id} from subnet")
            ec2.disassociate_route_table(AssociationId=assoc_id)
    
    print(f"Deleting route table: {rt_id}")
    ec2.delete_route_table(RouteTableId=rt_id)

# Delete subnets
subnets = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])['Subnets']
for subnet in subnets:
    subnet_id = subnet['SubnetId']
    print(f"Deleting subnet: {subnet_id}")
    ec2.delete_subnet(SubnetId=subnet_id)

# Finally, delete the VPC
print(f"Deleting VPC: {vpc_id}")
ec2.delete_vpc(VpcId=vpc_id)
print("VPC and all associated resources deleted successfully.")
