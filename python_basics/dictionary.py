#This is an example of dictionaries in Python
def main():
    #Dictionary of AWS services
    aws_services = {    
        "S3": "Simple storage service",
        "Lambda": "Serverless compute",
        "EC2": "Elastic Compute cloud",
    }

    print(f"Simple dictionary of Aws Services: {aws_services}")

    #Access the Value of a Key
    lambda_description = aws_services["Lambda"]
    print(f"Description of Lambda service is: {lambda_description}")

    #Modify a value
    aws_services["Lambda"] = "AWS Serverless compute Service"
    print(f"The new description of Lambda service is: {aws_services['Lambda']}")

    # Add a new entry to the dictionary
    aws_services["SNS"] = "Simple notification Service"
    print(f"Here's the updated dictionary: {aws_services}")

    # Remove an Entry from the dictionary
    del aws_services["Lambda"]
    print(f"Dictionary after deletion of Lambda: {aws_services}")

    #use of keys(), values() and items() methods:
    print(aws_services.keys())
    print(aws_services.values())
    print(aws_services.items()) #Returns in the form of tuples
    
    #Modify to create a nested dictionary
    aws_services["EC2"]={
        "description": "Elastic Compute Cloud",
        "launch_year": 2006,
    }
    print(f"Here's the nested dictionary: {aws_services['EC2']}")
if __name__ == "__main__":
    main()