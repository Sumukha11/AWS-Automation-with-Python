#Examples of loops in Python

def main():
    aws_services = ["S3","Lambda", "EC2", "DynamoDB"]
   

   #use a for loop to iterate through the list
    #for service in aws_services:
       #print(service)
    
    #use a while loop to iterate through the list
    index = len(aws_services) - 1
        
    while index >= 0:
        #print(aws_services[index])
        index -= 1

    #Enumerate funtion to iterate through the list with index
    for index, service in enumerate(aws_services):
        print(f"Service no.{index + 1}: {service}")

if __name__== "__main__":
    main()