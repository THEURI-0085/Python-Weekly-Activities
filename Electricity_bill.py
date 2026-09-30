# Define a function to calculate electricity bill
def calculate_bill(units_consumed, cost_per_unit):
    bill = units_consumed * cost_per_unit
    return bill
# Ask the user to enter the required information
units_consumed = float(input("Enter units consumed: "))
cost_per_unit = float(input("Enter cost per unit: "))

# Call the function
total_bill = calculate_bill(units_consumed, cost_per_unit)

#Display the calculated electricity bill
print(f"Electricity Bill: Ksh {total_bill:.2f}")
