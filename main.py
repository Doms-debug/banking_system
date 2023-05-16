class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("Personal details")
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print(f"Account balance has been updated: {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Insufficient funds. Balance available: {self.balance}")
        else:
            self.balance = self.balance - self.amount
            print(f"Account balance has been updated: {self.balance}")

    def view_balance(self):
        self.show_user_details()
        print(f"Account balance: {self.balance}")


Dominik = Bank("Dominik", 20, "male")
Dominik.deposit(200)
Dominik.withdraw(100)
Dominik.view_balance()

