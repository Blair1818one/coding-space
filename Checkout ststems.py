def display_items():
    """Display the list of items and their price."""
    print("ltems available for purchase:")
    print("1. Rice: 5000 UGX per kg")
    print("2. Suger: 4000 UGX per kg")
    print("3. cooking oil: 8000 UGX per kg")
    print("pease enter the quantity for each item (0 or positive number).")

def get_quantity(item_name):
    """prompt for quantity of the item  and validate input."""
    while True:
        try:
            quantity = int(input(f"Enter quantity for {item_name}: "))
            if quantity < 0:
                print("quantity cannot be negative. please enter a valid quantity.")
            else:
                return quantity
        except ValueError:
            print("Invalid input. please enter a positive inter.")

def calculate_total(rice_qty, suger_qty, oil_qty):
    """Calculate the total bill and apply discount if eligible."""
    rice_price =5000
    sugar_price = 4000
    oil_price =8000

    subtotal =(rice_qty * rice_price) + (suger_qty * sugar_price) + (oil_qty * oil_price)
    discount = 0

    if subtotal > 50000:
        discount = subtotal * 0.07

    total = subtotal - discount
    return subtotal, discount, total

def main():
    """Main function to run the supermark builling system."""
    while True:
           customer_name = input("Enter customer's name (or type 'exit' to finish):")
           if customer_name.lower() == "exit":
               print("Exiting the program. thank you!")
               break
           
           display_items()
           
           rice_qty = get_quantity("Rice")
           sugar_qty = get_quantity("sugar")
           oil_qty = get_quantity("cooking oil")

           subtotal, discount, total = calculate_total(rice_qty, sugar_qty, oil_qty)

           # Display summary  
           print("\n---- Bill Summary----")
           print(f"Customer's Name: {customer_name}")
           print(f"quantity of Rice: {rice_qty} kg")
           print(f"quantity of sugar: {sugar_qty} kg")
           print(f"quantity of cooking oil: {oil_qty} liters")
           print(f"subtotal before discount: {subtotal} UGX")
           if discount > 0:
               print(f"Discount applied: {discount} UGX")
           print(f"Final total to pay: {total} UGX")
           print("----------------------------\n")

        
if __name__ == "__main__":
          main()
          
