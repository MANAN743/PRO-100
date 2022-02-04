class ATM():
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account


    def check_balance(self):
        print("Your balance is :-")
        print("SBI = 5000")
        print("Airtel Wallet = 500")

    def withdrawl1(self,SBI):
        new_amount = 5000 - SBI
        print("You have withdrawn amount "+str(SBI) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl2(self,AirtelWallet):
        new_amount = 500 - AirtelWallet
        print("You have withdrawn amount "+str(AirtelWallet) + ". Your remaining balance is "+ str(new_amount))
        


def main():
    print("Welcome to SBI Bank!")
    Account = input("Please enter your acount number: ")
    Card_number = input("Insert your card number:- ")
    pin_number  = input("Enter your pin number:- ")
    new_user =  ATM(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. SBI")
        print("2. Airtel Wallet")
        choose = int(input("Select your choice:- "))
        if (choose == 1):
           SBI = int(input("Enter the amount:- "))
           new_user.withdrawl1(SBI)
        if (choose == 2):
           AirtelWallet = int(input("Enter the amount:- "))
           new_user.withdrawl2(AirtelWallet)    
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()
