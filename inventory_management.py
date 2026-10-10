# This program manages product quantities using a dictionary
# Create a dictionary containing five products and their quantities
inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 8,
    "printer": 5
    }
# Display the quantity of a specified product
print("Quantity of Mouse:",
      inventory["Mouse"])
# Add a new product to the inventory
inventory["USB Cable"] =30
print(inventory)
# Update the quantity of an existing product
inventory["Laptop"] = 15
print(inventory)
# Remove one product from the inventory
del inventory["printer"]
print(inventory)
# Display the final inventory
print("\n Final inventory:")
print(inventory)
