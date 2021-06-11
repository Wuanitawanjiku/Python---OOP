Trials = 3
UserPin = 1234

while Trials !=0:
    Pin = int(input("Input Pin: "))
    if Pin != UserPin:
        Trials -= 1
        print("Try again, wrong input pin")
    else:
        UserChoice = input("d: Deposit or w: Withdraw: ")
        if UserChoice == "d":
            UserDeposit = input("Enter amount to deposit: ")
            print(UserDeposit, "Has been deposited")
        if UserChoice == "w":
            UserWithdraw = input("Amount to be withdrawn: ")
            print(UserWithdraw, "Money has been withdrawn from your account")
        UserExit = input("Continue? Y/N: ")
        if UserExit == "N":
            print("Thank you for using our bank")
            break
        else:
            continue