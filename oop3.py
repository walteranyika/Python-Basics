# classes
# Customer - names, email, kra, dob, gender
# BankAccount - Customer, acc_no, acc_type, balance

class Customer:
    def __init__(self, names: str, email: str, kra: str, dob: str, gender: str):
        self.names = names
        self.email = email
        self.kra = kra
        self.dob = dob
        self.gender = gender

    def show_details(self):
        print(f"Name : {self.names} and KRA PIN : {self.kra}")
        # return f"Name : {self.names} and KRA PIN : {self.kra}"

    def __str__(self):
        return f"{self.names} {self.gender}"


class Account:
    def __init__(self, owner: Customer, acc_no: str, acc_type: str, balance: float):
        self.owner = owner
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("***************")

    def deposit(self, amount: float):
        self.balance += abs(amount)

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= abs(amount)

    def __str__(self):
        return f"Account No {self.acc_no} for {self.owner.names}"


owner1 = Customer("Jim Jong", "jj@test.com", "KRA001", "31-8-2000", "M")
owner2 = Customer("Yuang Ti", "yt@test.com", "KRA002", "19-11-1995", "F")

acc1 = Account(owner1, "98765", "current", 80_000)
acc2 = Account(owner1, "98766", "savings", 1_000_000.50)
acc3 = Account(owner2, "98767", "savings", 71_000.00)

# print(owner1.dob) # private
# print(owner1.show_details())

acc1.print_details()
acc1.deposit(-9000)
acc1.print_details()
acc1.withdraw(1_000)
acc1.print_details()

print(owner1)
print(acc1)
