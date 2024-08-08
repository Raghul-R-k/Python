class BankAccount:
    current_amount = 1000
    def __init__(self):
        self.Name = ""
   

    @staticmethod
    def Withdraw():
        withdraw_amount = 300
        print(f'Initial amount {BankAccount.current_amount}')
        BankAccount.current_amount -= withdraw_amount
        BankAccount.current_amount = BankAccount.current_amount
        print(f'Remaining balance {BankAccount.current_amount}')
    
    def Deposit(self):
        deposit_amount = int(input('Enter Amount to Deposit: '))
        self.current_amount += deposit_amount
        print(f'Balance: {self.current_amount}')

user = BankAccount()
BankAccount.Withdraw()
user.Deposit()