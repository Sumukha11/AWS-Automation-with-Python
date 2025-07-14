#Learning Boto3 setup script
#sudo apt-get install python3-pip
#pip3 install boto3

import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)