#Examples of Exception handling in Python

def main():
    service = "EKS"
    service_status = get_service_status(service)
    if service_status:
        print(f"{service} service status is: {service_status}")

        if service_status == "Operational":
            print(f"performing operation on {service}.")
        else:
            print(f"{service} is not operational, cannot perform operation.")
    else:
        print("Service Status not found.")
    #use exception handling to check if a service is present in the dictionary

def get_service_status(service_name):
    #Dictionary of AWS services
    aws_services_status = {
        "EC2": "Maintenance",    
        "S3": "Available",
        "Lambda": "Issues Detected",
        "DynamoDB": "Operational",
        "RDS": "Operational",
    }
    try:
        return aws_services_status[service_name]
    except KeyError as ke:
        print(f"ERROR: {ke}. Status for AWS service {service_name} is not available.")

if __name__ == "__main__":
    main()
