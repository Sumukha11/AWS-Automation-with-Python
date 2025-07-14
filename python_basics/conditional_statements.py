#Examples of conditional statements in Python
def main():
    user_requirement ="file_storage"

    if user_requirement == "file_storage":
        aws_service = "S3"
    elif user_requirement == "virtual_server":
        aws_service = "EC2"
    elif user_requirement == "serverless_computing":
        aws_service = "Lambda"
    else:
        aws_service = "Unkown service"
    #Condition to check what should be printed
    if aws_service != "Unkown service":
        print(f"provisioning the resource {aws_service}.")
    else:
        print(" The service mentioned is unknown.")

if __name__ == '__main__':
    main()