print ("Welcome to UBI bank ATM")
restart='Y'
count=2
chances=3
balance=11000
password=1432
class Person:
    new_balance=balance
    def __init__(self) -> None:
        pass
    def balance_check(self):
        print(f"Your account balance is {self.new_balance}.")
    def withdraw(self,amount)->float:
        self.new_balance=self.new_balance-amount
        return self.new_balance
    def add_amount(self,amount)->float:
        self.new_balance=self.new_balance+amount
        return self.new_balance
a=Person()

while chances>0: 
    pin=int(input("Enter your 4 digit pin : "))
    if pin==password:
        while restart not in ('n','No','no','N'):
            print("Check balance enter 1")
            print("Check withdraw enter 2")
            print("Check add balace enter 3")
            print("Enter no for exit.")
            choice=input()
            if choice=='1':
                a.balance_check()
            elif choice=='2':
                print("Enter your amount ")
                amount=int(input())
                while amount%500!=0:
                    print("Oops! Invalid amount.")
                    print("Enter a valid amount.")
                    if count>0:
                        amount=int(input())
                        count-=1
                    else:
                        print("Thanks for using me.")
                        exit()
                balance=a.withdraw(amount)
                print("You succesfully withdraw")
                print(f"The rest of the amount in your account is {balance}")
            elif choice=='3':
                print("Enter your amount ")
                amount=int(input())
                balance=a.add_amount(amount)
                print("You add amount succesfully ")
                print(f"The amount in your account is {balance}")
            elif choice=='no'or choice=='n':
                print("Thanks for using me.\n Have a good day")
                exit()
            else:
                print("Oops! worng option.")
                print("Want to continue select y or for break select n.")
                continues=input()
                if continues=='y':
                    continue
                break

    else:
        print("Worng password")
        chances-=1
else:
    print("Your card block for next 24 hours") 
    print("Thanks for using me.\n Have a good day")
    exit()        
