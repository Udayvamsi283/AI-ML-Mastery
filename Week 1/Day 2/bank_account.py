class bank:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")
    def check_balance(self):
        print(f"Current Balance: {self.balance}")

# Example usage:
if __name__ == "__main__":
    my_account = bank()
    my_account.deposit(1000)
    my_account.withdraw(200)
    my_account.check_balance()