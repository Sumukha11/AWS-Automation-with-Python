import boto3
import csv


#Funtion for the API Call.

def get_international_taxes(valid_product_lines, billing_bucket, csv_file):
    try:
        raise Exception("API failure: International Taxes API is currently Unavailable.")
    except Exeception as error:
        sns=boto3.client('sns')
        sns_topic_arn="arn:aws:sns:ap-south-1:750067408701:TaxesApiConnectionError" #ARN of the SNS topic
        message=f"Lambda function failed to reach internation taxes API for '{billing_bucket}' bucket and file '{csv_file}'. ERROR: '{error}'."
        sns.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject="Lambda API Call Failure"
        )

        print("Published failure to sns topic")
        raise error