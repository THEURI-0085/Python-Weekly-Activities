class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current Balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)


# Creating an object
account1 = BankAccount("ACC101", 5000, "2024-03-10", "Kamau")

# Calling the methods
print("Deposited Amount:", account1.deposit(2000))
print("Withdrawn Amount:", account1.withdraw(1000))
account1.check_balance()
account1.customer_details()
