# This program manages employee salaries using a dictionary
# Create a dictionary containing five employees and their salaries
employees = {
    "Kelvin": 40000,
    "Mary": 48000,
    "Moha": 25000,
    "Jane": 35000,
    "George": 50000
    }
# Display all employee names and salaries using a loop
print("Employee Salary Records:")
for name, salary in employees.items():
    print(f"{name}: Ksh {salary:.2f}")
# Update the salary of one employee
employees["Moha"]= 30000
print(employees)
# Add a new employee and salary
employees["Pauline"]=17000
print(employees)
# Calculate the total salary payable to all employees
total_salary = sum(employees.values())
# Display the updated employee records
print("\n Updated Employee Salary Records:")
for name, salary in employees.items():
    print(f"{name}: Ksh {salary:.2f}")

# Display the total salary payable
print(f"\n Total Salary payable: Ksh {total_salary:2f}")
