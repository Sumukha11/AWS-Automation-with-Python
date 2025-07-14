#Import boto3 library
import boto3
import time

#Instantiate a boto3 resource for S3
s3 = boto3.resource('s3')
timestamp = int(time.time())
# Create a unique bucket name using the current timestamp
bucket_name = f'dct-crud-sumukha-{timestamp}'
# Define the region where the bucket will be created
region = "ap-south-1"

#Check if the bucket exists and create it if it doesnt exist
all_my_buckets = [bucket.name for bucket in s3.buckets.all()] #s3.bucket.all() returns a bucket object, buy doing bucket.name we get the name string of the bucket.
if bucket_name not in all_my_buckets:
    print(f"{bucket_name} doesn't exist, creating a new bucket...")
    # Only include LocationConstraint if region is NOT us-east-1
    s3.create_bucket(
        Bucket = bucket_name,
        CreateBucketConfiguration = {'LocationConstraint': region}
        )
    print(f"{bucket_name} bucket has been created successfully.")

else:
    print(f"{bucket_name} already exists.")


#Create file_1 and file_2
file_1 = 'file_1.txt'
file_2 = 'file_2.txt'

#Upload files to the bucket
s3.Bucket(bucket_name).upload_file(Filename = file_1, Key = file_1)

#Read and print the file from the bucket
obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

# Update file_1 with the file_2 data
s3.Object(bucket_name, file_1).put(Body = open(file_2,'rb'))
obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

#Delete the file from the bucket
s3.Object(bucket_name, file_1).delete()
print(f"file_1 has been deleted from the bucket {bucket_name}.")

#Delete the bucket (Bucket should be empty)
bucket = s3.Bucket(bucket_name)
bucket.delete()
print(f"Bucket {bucket_name} has been deleted.")
