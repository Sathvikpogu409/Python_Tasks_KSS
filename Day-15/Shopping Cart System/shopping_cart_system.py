cart = ["Apple", "Milk", "Bread", "Apple"]

cart = set(cart)

prices = {
    "Apple": 30,
    "Milk": 50,
    "Bread": 40
}

total = 0

for item in cart:
    try:
        if item in prices:
            total += prices[item]
            print(item, prices[item])
        else:
            print("Item not found:", item)

    except Exception as e:
        print("Error:", e)

print("Total cost:", total)
