#Develop a system with one function that prompts a user to enter name, pin and once a pin is valid. 
    #When pin is  correct ask  user to enter an amount to withdraw and system should be able to determine if the user has sufficient 
    # bal then the system should be able to reduce the balance on the account.
    # Account bal should be displayed after withdraw.

#By Malinga Robert $ Mugisha Ronald
actualbalance = 200000
def atm():
    name = input("Please enter your name:")
    pin = input("Please enter your pin:")
    if pin != "2244":
        print("Your pin is invalid")
        pin = input("Please enter the correct pin:")
    amount = input("Enter amount to withdraw:")
    if int(amount) > actualbalance:
        print("You have insuffitient funds")
        amount = input("Enter valid amount to withdraw:")
    balance = actualbalance - int(amount)
    print ("You have withdrawned:" ,int(amount))
    print ("Your current balance is:" , balance)
atm()
