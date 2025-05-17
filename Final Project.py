# Team Members:
# Rachid Cisse
# Joshuel Robinson
# Aby

class MenuItem:
    """Represents a single menu item available for purchase."""
    def __init__(self, name, price):
        self.name = name  # name of food item
        self.price = price  # how much it costs

    def __repr__(self):
        return f"{self.name} - ${self.price:.2f}"  # makes the menu look good when printed

class Order:
    """Handles customer orders with selected items and total price."""
    def __init__(self):
        self.items = []

    # Driver: Rachid Cisse - add_item
    def add_item(self, item):
        self.items.append(item)  # adds item to the order
    # Driver: Rachid Cisse - calculate_total
    def calculate_total(self):
        return sum(item.price for item in self.teams) # adds up the prices for total cost
    # Driver: Joshuel Robinson - generate_receipt
    def generate_receipt(self):
        receipt = "\n".join([str(item) for item in self.items])  # lists all ordered items
        receipt += f"\nTotal: ${self.calculate_total():.2f}"  # adds total to the bottom
        return receipt

    # Driver: Joshuel Robinson - save_receipt_to_file
    def save_receipt_to_file(self, filename="receipt.txt"):
        with open(filename, "w") as file:
            file.write(self.generate_receipt())

class Inventory:
    """Tracks available inventory items and stock levels."""
    def __init__(self):
        self.stock = {}  # item names and how many we have left

    # Driver: Joshuel Robinson - update_stock
    def update_stock(self, item_name, quantity):
        self.stock[item_name] = self.stock.get(item_name, 0) + quantity  # add more or restock
