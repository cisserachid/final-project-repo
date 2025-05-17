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
    # Driver: Aby - is_in_stock
    def is_in_stock(self, item_name):
        return self.stock.get(item_name, 0) > 0  # returns True if at least one left

    # Driver: Aby - reduce_stock
    def reduce_stock(self, item_name, quantity=1):
        if self.is_in_stock(item_name):
            self.stock[item_name] -= quantity  # subtract the quantity ordered
            return True
        return False  # nothing to reduce if out of stock

    # Driver: Aby - display_stock
    def display_stock(self):
        return "\n".join([f"{item}: {qty} left" for item, qty in self.stock.items()])  # shows remaining stock

# Driver: Aby - run_order_system
def run_order_system():
    menu = {
        "Taco": MenuItem("Taco", 3.50),
        "Burrito": MenuItem("Burrito", 6.00),
        "Soda": MenuItem("Soda", 1.50)
    }

    inventory = Inventory()
    inventory.update_stock("Taco", 5)
    inventory.update_stock("Burrito", 3)
    inventory.update_stock("Soda", 10)

    print("Welcome to the Food Truck!")
    print("Menu:")
    for item in menu.values():
        print(item)

    print("\nCurrent Inventory:")
    print(inventory.display_stock())

    order = Order()

    while True:
        choice = input("\nEnter item name to order (or 'done' to finish): ").strip()
        if choice.lower() == "done":
            break
        elif choice in menu:
            if inventory.is_in_stock(choice):
                order.add_item(menu[choice])
                inventory.reduce_stock(choice)
                print(f"{choice} added to order.")
            else:
                print("Sorry, that item is out of stock.")
        else:
            print("Invalid item. Please choose from the menu.")

    print("\n--- Receipt ---")
    receipt = order.generate_receipt()
    print(receipt)

    # Save receipt to a file
    order.save_receipt_to_file()
    print("Receipt saved to 'receipt.txt'.")

    print("\nRemaining Inventory:")
    print(inventory.display_stock())

if __name__ == "__main__":
    run_order_system()
