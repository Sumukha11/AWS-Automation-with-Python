import boto3
import io 
import csv
import logging

#Boto3 cLients 
s3_client=boto3.client('s3')
rds_client=boto3.client('rds-data')

#Dictionary to convert currency to USD
currency_conversion_to_usd = {'USD':1, 'CAD':0.79, 'MXN': 0.05}
database_name=''#Need to create a Aurora DB 
secret_store_arn=''
db_cluster_arn=''


#Configure logging
logger=logging.getlogger()
logger.setLevel(logging.INFO)

def process_record(record):
    id, company_name, country, city, product_line, bill_date, bill_amount, currency = record
    bill_amount = float(bill_amount)

    #convert the bill amount to USD
    rate=currency_conversion_to_usd.get(currency)

    if rate:
        usd_amount=bill_amount*rate
    else:
        logger.ifno(f"No rates found for the currency: {currency}")

#prepare the SQL statements with placeholders for inserting record into the database
sql_statement=("INSERT IGNORE INTO billing_data"
                    "(id,company_name, country, city, product_line, "
                    "item, bill_date, currency, bill_amount, bill_amount_usd)"
                    "VALUES(:id, :company_name, :country, :city, :product_line"
                    ":item, :bill_date, :currency, :bill_amount, :usd_amount)"
                    
)

# preparing the parameters for SQL statement
sql_parameters=[
    {'name':'id','value':{'stringValue':id}},
    {'name':'company_name','value':{'stringValue':company_name}},
    {'name':'country', 'value':{'stringValue':country}},
    {'name':'city','value':{'stringValue':city}},
    {'name':'product_line','value':{'stringValue':product_line}},
    {'name':'item','value':{'stringValue':item}},
    {'name':'bill_date','value':{'stringValue':bill_date}},
    {'name':'currency','value':{'stringValue':currency}},
    {'name':'bill_amount','value':{'stringValue':bill_amount}},
    {'name':'usd_amount','value':{'stringValue':usd_amount}},
]

#Execute the SQL statement and log the response
response=execute_statement(sql_statement, sql_parameters)
logger.info(f"SQL execution response: {response}")

def execute_statement(sql, sql_parameters):
    try:
        response=rds_client.execute_statement(
            secretArn=secrets_store_arn,
            database=database_name,
            ResourceArn=db_cluster_arn,
            sql=sql,
            parameters=sql_parameters
        )
    except Exception as e:
        logger.error("ERROR: Could not connect to Aurora Serverless MySQL instance.")
        return None

def lambda_handler(event,context):

    try:
        # Get the bucket name and file name from the event
        bucket_name=event['Records'][0]['s3']['bucket']['name']
        s3_file=event['Records'][0]['s3']['object']['key']

        #Read the csv file from S3
        response=s3_client.get_object(Bucket=bucket_name, Key=s3_file)
        data=response['Body'].read().decode('utf-8')


        #Use csv reader to process the CSV file
        csv_reader=csv.reader(io.StringIO(data))
        next(csv_reader)

        #Process each record in the CSV file
        for record inm csv_reader:
            print(record)
        
        logger.info("Lambda has finished execution.")

    except Exection as e:
        logger.info(f"ERROR:{e}")

    