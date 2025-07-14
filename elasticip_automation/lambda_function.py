import boto3

def lambda_handler(event, context):
    ec2_lambda-boto3.resource('ec2')

    for elastic_ip in ec2_resources.vpc_addresses.all():
        if elastic_ip.instance_id is None:
            print(f"No association for the Elastic IP: {elastic_ip}. Releasing...")
            elastic_ip.release()

    return {
        'statusCode': 200,
        'body': 'Processed elastic IPs'
    }
