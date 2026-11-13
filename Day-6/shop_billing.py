# Create a menu-driven shop billing program using a dictionary for product
# names and prices, a list for cart items, a set for product categories,
# and tuples for product details. Define functions to display products,
# add items to the cart, and calculate the total bill. Use recursion to
# calculate the total price and handle ValueError, ZeroDivisionError,
# TypeError, and NameError exceptions.



# Product names and prices stored in a dictionary
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}

# Product categories stored in a set
categories = {"Stationery", "Writing", "School Supplies"}

# Product details stored in tuples
product_details = (
    ("Pen", 10),
    ("Notebook", 50),
    ("Pencil", 5)
)

# Cart stored in a list
cart = []


# Recursive function to calculate total bill
def calculate_total(items):
    if not isinstance(items, list):
        raise TypeError

    if len(items) == 0:
        return 0

    product, quantity = items[0]

    if not isinstance(product, str) or not isinstance(quantity, int):
        raise TypeError

    return products[product] * quantity + calculate_total(items[1:])


# Function to display products
def display_products():
    print("Available Products:")
    for product, price in products.items():
        print(product, ":", price)


# Function to add items to cart
def add_to_cart():
    product = input("Enter product name: ")

    try:
        if product not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError

        cart.append((product, quantity))
        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    except NameError:
        print("Product not found in store.")


# Function to calculate and display total bill
def view_total_bill():
    if len(cart) == 0:
        print("Cart is empty.")
        return

    try:
        print("Items in Cart:")

        for product, quantity in cart:
            print(product, "x", quantity)

        total = calculate_total(cart)
        print("Total Bill:", total)

        # Handle division by zero if needed
        average = total / len(cart)

    except TypeError:
        print("Cart data type error.")

    except ZeroDivisionError:
        print("Calculation error: division by zero.")


# Main menu
while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            view_total_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice! Please enter 1 to 4.")

    except ValueError:
        print("Please enter a valid menu choice.")
