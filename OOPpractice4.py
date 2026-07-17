class BankAccount:

    def __init__(self,AccountNum,Balance):

        self.AccountNum = AccountNum
        self.Balance = Balance

    def Display(self):
        print("Enter account number:",self.AccountNum)
        print("Enter the balance :",self.Balance)

    def Deposit(self):
        Deposit = int(input("Enter the amount :"))

        self.Balance = self.Balance + Deposit

        print("Balance is :",self.Balance)

    def Withdraw(self):

        Withdraw = int(input("Enter the amount that you withdraw :"))

        if Withdraw <= self.Balance:
            self.Balance = self.Balance - Withdraw
            print("Remaining balance is :",self.Balance)

        else:
            print("Insufficint balance to withdraw ")

obj = BankAccount(12345, 10000)
obj.Display()
obj.Deposit()
obj.Withdraw()


