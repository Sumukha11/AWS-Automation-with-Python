# Shows the examples of lists in Python
def main():
    aws_services = ["S3","Lambda", "EC2", "DynamoDB"]
    print(f"AWS services list: {aws_services}")
    first_item = aws_services[0]
    #Print the first service name
    print(f"The first item in the list is: {first_item}.")
    #Print the last service name
    last_item = aws_services[-1]
    print(f"The last item in the list is: {last_item}.")
    #Modify any of the items in the list
    aws_services[-1] = "SNS"
    print(f"The new last item in the list is: {aws_services[-1]}")
    #Add a new item to the list
    aws_services.append("VPC")
    print(f"New item has been added to the list: {aws_services}")
    #Removing an item from the list
    aws_services.pop(2)
    print(f"Heres the new item after the pop operation: {aws_services}")
    #Here's how to slice the list   
    sliced_list = aws_services[0:3]
    print(f"Here's the sliced list: {sliced_list}")
    #Find the length of the list
    list_len = len(aws_services)
    print(f"Length of our list is: {list_len}")
    
if __name__ == "__main__":
    main()
