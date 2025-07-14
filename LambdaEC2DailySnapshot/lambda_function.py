import json
import boto3
import logging
from datetime import datetime

logger=logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2=boto3.client('ec2')
    current_date=datetime.now().strftime("%Y-%m-%d")

    try:
        print("Entered try block")
        response=ec2.create_snapshot(
            VolumeId='vol-0e0f7cb68477a0792',
            Description='My EC2 Snapshot',
            TagSpecifications=[
                {
                    "ResourceType":"snapshot",
                    'Tags':[
                        {
                            'Key':'Name',
                            'Value':f'My EC2 Snapshot {current_date}'
                        }
                    ]
                    }
            ]
        )
        print("Exited try block")
        logger.info(f"Successfuly created snapshot: {json.dumps(response, default=str)}")

    except Exception as e:
        logger.error(f"Error creating snapshot: {str(e)}")



if __name__ == "__main__":
    lambda_handler({}, None)
