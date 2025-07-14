#Examples of a functions in Python

def main():
    #Determine the shoe type using the materials used
    materials_1 = ["Leather", "Rubber"]
    materials_2 = ["Canvas", "Rubber"]

    #Use the create_shoe function
    shoe_1 = create_shoe(materials_1)
    shoe_2 = create_shoe(materials_2)

    print(f"Shoe is of type: {shoe_2['type']}")

def create_shoe(materials_list):
    shoe_type = " "

    if 'Leather' in materials_list and "Rubber" in materials_list:
        shoe_type = "boots"
    elif 'Canvas' in materials_list and "Rubber" in materials_list:
        shoe_type = "sneakers"
    return {'type': shoe_type}
    

if __name__ == "__main__":
    main()