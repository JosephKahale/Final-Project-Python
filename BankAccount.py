class BankAccount():
    def __init__(self, fullname, accountNumber, balance) -> None:
        self.fullname = fullname
        self.accountNumber = accountNumber

    def getAccountNumber(self):
        return self.accountNumber
    
    def getFullName(self):
        return self.fullname
    
    def withdraw(self):
        pass
    
    def deposit(self):
        pass