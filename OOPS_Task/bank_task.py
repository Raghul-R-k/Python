#Instance Variable : Name,Amount,Address,Account No 
#Instance Mathod : CreateAccount() , DisplayAccountInfo()
#Class Variable :Bank_Name,ROI_on_FD
#Create a class MEthod :Bank Info


class Bank:
    Bank_Name = 'Axis Bank'
    ROI_on_FD = '12%'
    
    def __init__(self):
        self.name = ""
        self.amount = 0
        self.address = ""
        self.accountNo = 0
    
    @staticmethod
    def DisplayKYCInfo(customer_name, customer_photo, address):
        print(f"Customer AAdhar: {customer_name}")
        print(f"Customer Photo: {customer_photo}")
        print(f"Address: {address}")

    def CreateAccount(self):
        self.name = input('Enter Your Name : ')
        self.amount = input('Enter Your Amount : ')
        self.address = input('Enter Your Address : ')
        self.accountNo = input('Enter Your Account Number : ')

    def DisplayAccountInfo(self):
        print(f'Name : {self.name} \nAmount : {self.amount} \nAddress : {self.address} \nAccount Number : {self.accountNo} ')

    @classmethod
    def bank_info(cls):
        print("Bank Name :",cls.Bank_Name)
        print("Rate of Interest :",cls.ROI_on_FD)

        
Bank.DisplayKYCInfo('102211202121', 'Photo', 'Chennai')
def main():
    user1 = Bank()
    print("_____________Creating the first User_________")
    user1.CreateAccount() 
    print()
    user1.DisplayAccountInfo()
    user1.bank_info()
if __name__ == '__main__':
    main()


