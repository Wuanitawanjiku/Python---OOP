#3 attributes and 3 methods 
#Amount must be greater than 0 and less than balance plus transaction fee
#Amount>0, no outstanding loan, amount requesting is less than loan limit
#attributes :loan, loan limit, loan fees


class Account:
    
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
        self.balance = 0
        self.transaction_fee = 23
        self.loan_limit = 30000
        self.loan_fees = 3
        self.loan_amount = 0


    def deposit(self, amount):
        if amount <=0:
            return "Please deposit a valid amount"
        else:
            self.balance += amount
            return f"Hello {self.name}, you have deposited {amount}. Your current balance is {self.balance}"

    def withdraw(self, amount):
        total = amount + self.transaction_fee
        if amount <=0:
            return "Cannot withdraw zero or less"
        elif total > self.balance:
            return "Amount cannot be withdrawn if balance is less than amount"
        else:
            self.balance -= total
            return f"Hello {self.name}, you have successfully withdrawn {amount}, current account balance {self.balance}"

    def borrow(self, amount):
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
            return f"Hello {self.name}, you have borrowed {amount} your outstanding loan is {self.loan_amount} and your current balance is {self.balance + amount}"