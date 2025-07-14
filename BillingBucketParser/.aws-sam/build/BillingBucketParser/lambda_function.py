import json
import csv
import boto3
from datetime import datetime

def lambda_handler(event, context):
    #Initialize the S3 resource using boto3
    s3=boto3.resource('s3')

    #Extract the bucket name and CSV file name from the 'Event' input
    billing_bucket=event['Records'][0]['s3']['bucket']['name']
    csv_file=event['Records'][0]['s3']['object']['key']

    #define the name of the error bucket
    error_bucket='sumukha-billing-x-errors'

    #Download the CSV file from S3
    obj=s3.Object(billing_bucket, csv_file)
    data=obj.get()['Body'].read().decode('utf-8').splitlines()

    #Initialize a flag (error_found) to false. We'll set this flag to true when we find an error
    error_found=False

    #Define valid product lines and valid currencies
    valid_product_lines=['Bakery','Veggies','Dairy']
    valid_currencies=['USD','MXN','CAD']

    #Read the CSV file line by line using the pythons csv reader. ignore the header line(data[1:])
    for row in csv.reader(data[1:], delimiter=","):
        
        # for each row extract all the data
        date=row[6]
        product_line=row[4]
        currency=row[7]
        bill_amount=float(row[8])

        #Check if the product line is valid
        if product_line not in valid_product_lines:
            error_found=True
            print(f"Error in record {row[0]}: unrecognized product line.")
            break
        #check if the currency is valid
        if currency not in valid_currencies:
            error_found=True
            print(f"Error in record {row[0]}: unrecognized currency type.")
            break
        #Check if the bill amount is valid
        if not isinstance(bill_amount,(float)):
            error_found=True
            print(f"Error in Record {row[0]}: incorrect Bill amount data.")
            break
        #Check if the date and time are valid
        try:
            datetime.strptime(date,'%Y-%m-%d')
        except ValueError:
            error_found=True
            print(f"Error found incorrect date format: {date}")
            break
        
        #After checking all rows, if an error is found, copy the CSV file to the error bucket and delete in the original bucket
    if error_found:
        copy_source={
            'Bucket':'sumukha-billing-x',
            'Key':csv_file
        }
        try:
            s3.meta.client.copy(copy_source, error_bucket, csv_file)
            print(f"Moved errenous file to: {error_bucket}.")
            s3.Object(billing_bucket, csv_file).delete()
            print("Deleted original file from bucket.")
        except Exception as e:
            print(f"Error while moving file: {str(e)}.")
    else:
        return{
            "statusCode":200,
            "body":"No Errors found in the CSV file!",
        }