#Amount must be greater than 0 and less than balance plus transaction fee
#Amount>0, no outstanding loan, amount requesting is less than loan limit
#attributes :loan, loan limit, loan fees
#Ability to transfer to another account

from datetime import date, datetime
class Account:
    
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
        self.balance = 0
        self.transaction_fee = 23
        self.loan_limit = 30000
        self.loan_fees = 3
        self.loan_amount = 0
        self.transactions = []
        self.withdrawal_transactions = []
        self.loan_transactions = []
        self.repaid_transactions = []        


    def deposit(self, amount):
        try:
            amount + 10
        except TypeError:
            return f"Input amount in figures"
        if amount <=0:
            return "Please deposit a valid amount"
        else:
            self.balance += amount
            transaction = {"amount":amount, "balance":self.balance, "narration":"You deposited", "time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello {self.name}, you have deposited {amount}. Your current balance is {self.balance}"

    def withdraw(self, amount):
        try:
            amount -10
        except TypeError:
            return f"Enter amount to be withdrawn in figures"
        total = amount + self.transaction_fee
        if amount <=0:
            return "Cannot withdraw zero or less"
        elif total > self.balance:
            return "Amount cannot be withdrawn if balance is less than amount"
        else:
            self.balance -= total
            withdrawaltransaction = {"amount":amount, "balance":self.balance, "narration":"You withdrew", "time":datetime.now()}
            self.withdrawal_transactions.append(withdrawaltransaction)
            return f"Hello {self.name}, you have successfully withdrawn {amount}, current account balance {self.balance}"

    def borrow(self, amount):
        try:
            amount + 10
        except TypeError:
            return f"Enter amount to be borrowed in figures"
        if amount <= 0:
            return "Failed loan cannot be offered"
        elif self.loan_amount > 0:
             return "Loan cannot be granted"
        elif amount > self.loan_limit:
            return "Amount cannot be borrowed"
        else:
            total_interest = self.loan_fees*amount/100
            total_loan = total_interest + amount
            self.loan_amount += total_loan
            loan_transactions = {"amount": amount, "balance":self.balance, "narration":"Your loan balance as of", "time":datetime.now()}
            self.loan_transactions.append(loan_transactions)
            return f"Hello {self.name}, you have borrowed {amount} your outstanding loan is {self.loan_amount} and your current balance is {self.balance + amount}"

    def repay(self, amount):
        try:
            amount + 10
        except TypeError:
            return f"Enter amount in figures"
        if amount < self.loan_amount:
            outstanding_balance = self.loan_amount - amount           
            return f"Loan not fully paid. Outstanding balance {outstanding_balance}"
        elif amount > self.loan_amount:
            extra_balance = amount - self.loan_amount
            extra_balance + self.balance
            return f"Loan fully paid and extra amount {extra_balance} has been updated to your account"
        else:
            amount == self.loan_amount  
            repaidtransactions = {"amount": amount, "balance": self.balance, "narration":"Amount paid", "time":datetime.now()}
            self.repaid_transactions.append(repaidtransactions)
            return "Outstanding balance is currently 0."


    def transfer(self, amount, account):
        try:
            amount +10
        except TypeError:
            return f"Input amount in figures"
        if amount <= 0:
            return f"Enter valid amount"
        fee = amount * 0.05
        amount = amount + fee
        if amount > self.balance:
                return f"Your balance is {self.balance} you need {amount} in order to transfer {amount}"
        else:
            self.balance -= amount
            account.deposit(amount)
            return f"Confirmed {amount} has been transfered to {account.name}.Your new balance is {self.balance}"



    def get_statement(self):
        for transaction in self.transactions:
            amount = transaction["amount"]
            narration = transaction["narration"]
            balance = transaction["balance"]
            time = transaction["time"]
            date = time.strftime("%D")
            print(f" {date}...{narration} ...{amount} ...balance {balance}")


class MobileMoneyAccount(Account):

    def __init__(self, name, phoneNumber, serviceProvider):
        Account.__init__(self, name, phoneNumber)
        self.serviceProvider = serviceProvider
        
    def buy_airtime(self, amount):
        try:
            amount + 10
        except TypeError:
            return f"Input amount in figures"
        if amount <=0:
            return "Insufficient funds to purchase airtime"
        else:
            self.balance -= amount
            transaction = {"amount":amount, "balance":self.balance, "narration":"You purchased airtime ", "time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello {self.name}, you have bought airtime worth {amount}. Your current balance is {self.balance}"

    

