# 🧠 Problem: Implement a Smart Shopping Cart Item using Dunder Methods

# Design a Python class called CartItem that represents an item in an online shopping cart.
# The class should demonstrate the use of multiple dunder (magic) methods to customize the behavior of objects.

# Each CartItem object should contain the following attributes:

# name → Name of the product

# price → Price of one unit of the product

# quantity → Number of units in the cart

# 📌 Requirements

# You must implement the following dunder methods in your class.

# 1️⃣ __init__(self, name, price, quantity)

# Initialize the object with the product name, price, and quantity.

# Example:

# item = CartItem("Laptop", 50000, 2)
# 2️⃣ __str__(self)

# Define a readable string representation of the object when printed.

# Example output:

# Laptop | Price: 50000 | Quantity: 2
# 3️⃣ __add__(self, other)

# Allow adding two CartItem objects to calculate the total price of both items combined.

# Example:

# item1 + item2

# Output:

# Total price of both items
# 4️⃣ __mul__(self, value)

# Allow multiplying an item with an integer to calculate the total cost for multiple sets.

# Example:

# item1 * 3

# Output:

# price × quantity × 3
# 5️⃣ __eq__(self, other)

# Two items should be considered equal if their prices are the same.

# Example:

# item1 == item2
# 6️⃣ __len__(self)

# Return the quantity of the item when len() is called.

# Example:

# len(item1)

# Output:

# quantity
# 7️⃣ __call__(self)

# Allow the object to behave like a function and return the total cost of the item.

# Example:

# item1()

# Output:

# price × quantity
# ⭐ Bonus Challenge (Advanced)

# Implement __getitem__(self, key) so that the attributes can be accessed like a dictionary.

# Example:

# item1["name"]
# item1["price"]
# item1["quantity"]

class Shopping_Cart:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    