class UserAccount():
    def __init__(self, fullname, address, phonenumber, creditScore) -> None:
        self.fullname = fullname
        self.address = address
        self.phoneNumber = phonenumber
        self.creditScore = creditScore

    def changeAddress(self, newAddress):
        self.address = newAddress

    def changeFullName(self, newName):
        self.fullname = newName

    def changePhone(self, newPhone):
        self.phoneNumber = newPhone

    def __str__(self) -> str:
        return self.fullname + "," + self.address + "," + self.phoneNumber + "," + self.creditScore
    