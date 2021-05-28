#three attributes and three methods 
class Bank:
    
    def __init__(self, deposit, withdraw, save):
        self.deposit = deposit
        self.withdraw = withdraw 
        self.save = save

    def new_customer(self):
        return f"The bank allows a new customer to deposit from a minimum of Ksh.{self.deposit}"

    def transaction(self): 
        return f"The bank allows one to withdraw upto a maximum amount of Ksh.{self.withdraw}"

    def savings(self):
        return f"For one to earn a membership card at our bank, savings have to be from Ksh.{self.save}"