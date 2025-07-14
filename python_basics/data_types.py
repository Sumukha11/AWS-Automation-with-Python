#Defining the basic data types in Python    
def main():
    #string(str)
    instance_type = "t2.micro"
    message = "My isntance are of type: "

    #integer(int)
    num_of_instances = 5
    hours_running = 10

    print(f"{message}{instance_type}. I have {num_of_instances} of them and they have been running for {hours_running} hours.")

    #defining a boolean
    instances_running = True
    print(f"Are my instances running? {instances_running}.")
    print(f"My variable is of type: {type(instance_type)}.")

    #Floating point number(float)
    instances_cost_per_hour = 0.25  #USD
    print(f"The price of running these instance per hour is {instances_cost_per_hour} USD.")

if __name__=='__main__':
    main()