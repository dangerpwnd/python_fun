class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())
    
    def withdraw(self, amount):
        self.balance=self.balance - amount
        
    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self, ):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# Declare base class
class Checking(Account):

    def __init__(self, filepath, fee):
        # Inheriting the class
        Account.__init__(self, filepath)
        # Subclass variable
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

# checking=Checking("bal.txt", 1)
# checking.transfer(200)
# print(checking.balance)

# checking=Checking("bal.txt")
# checking.transfer(200)
# print(checking.balance)

# checking=Checking("bal.txt")
# checking.deposit(150)
# checking.commit()
# print(checking.balance)

# account=Account("bal.txt")
# print(account.balance)
# account.withdraw(100)
# account.commit()
# print(account.balance)
# account.deposit(250)
# account.commit()
# print(account.balance)
