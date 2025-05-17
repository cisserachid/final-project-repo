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
        return sum(item.price for item in self.items)  # adds up the prices for total cost

