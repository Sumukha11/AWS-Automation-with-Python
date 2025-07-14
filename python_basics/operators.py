#This is an example of using operators in Python
def main():
    item_name = "Banana"
    quantity = 5
    discount_rate = 0.1
    eligible_items = "Orange Banana Carrot"
    item_price = 2

    #Arithmetic Operators
    subtotal = item_price * quantity
    print(f"Subtotal for {quantity} {item_name}(s): ${subtotal:.2f}")

    #Membership Operators
    if item_name in eligible_items:
        discount = subtotal * discount_rate
        print(f"Discount: ${discount:.2f}")

    #Comparison Operators
    was_discount_applied = discount > 0
    print(f"Was the discount applied?: {was_discount_applied}")

    #Logical Operators
    if item_name == "Banana" and quantity >= 5:
        print("Item is eligible for free shipping.")
    else:
        print("Item is not eligible for free shipping.")

if __name__ == '__main__':
    main()
