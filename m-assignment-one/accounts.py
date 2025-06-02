import datetime 
class Transaction:
    def __init__(self,date,amount,narration,transaction_type):
        self.date = date
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type

    def message(self):
        return f"Confirmed you have {self.narration} in your account on {self.date} "


class Account():
    def __init__(self, name,account_number):
        self.name = name
        self._balance = 0
        self.loan = 0
        self.is_frozen = True
        self.minimum_balance = 200
        self.transaction = []

    def get_deposit(self,amount,narration = "Deposit"):
        current_date = datetime.datetime.now()
        if amount <= 0:
            return f"Deposit amount must be positive"  
        else:
                    
            transaction = Transaction(current_date,amount,narration,"Deposit")
            self.transaction.append(transaction)
            self._balance += amount   

            print(f"Hello {self.name} you have {narration} {amount} your new balance is {self._balance} on {transaction.date}")


        
        

    def get_withdrawal(self,amount, narration= "Withdrawal"):
        current_date = datetime.datetime.now() 
        
        if  self._balance > amount and self.minimum_balance == 200:
            transaction = Transaction(current_date,amount,narration,"Withdrawal")

            self.transaction.append(transaction)
            self._balance -= amount
            return f"Hello {self.name} you have {narration} Kshs {amount} your new balance is Kshs{self._balance} on {transaction.date}"

        elif amount <= 0:
            return f"Withdrwable amount must be positive"

        else:
            return f"{amount} not withrawable your account balance is {self._balance} and your minimum account balance is {self.minimum_balance} {transaction.date}"

    def transfer(self,amount,other_account_name, narration= "Trasfer"):
        current_date = datetime.datetime.now() 
        transaction = Transaction(current_date,amount,narration,"Transfer")

        if amount > 0 and self._balance > amount and self.minimum_balance > 200:
            return "You have nsufficient funds in your account"
        else:
            self.get_withdrawal(amount)
            other_account_name.get_deposit(amount)
            self.transaction.append(transaction)
            self._balance -=amount
            return f"Hello {self.name} you have {narration} to {other_account_name} and your account balance is {self._balance} on {transaction.date}"
            


    def get_balance(self):
        balance = 0
        for transaction in self.transaction:
            if transaction.transaction_type == "Deposit":
                balance +=transaction.amount

            elif transaction.transaction_type == "Withdraw":
                balance -= transaction.amount

            elif transaction.transaction_type=="request loan":
                balance += transaction.amount

            elif transaction.transaction_type == "Repay loan":
                balance -= transaction.amount

            return f"Your {self.name} your account balance is {balance} "

  

        

    def request_loan(self,amount):
        loan_amount = self.balance*3      
        if amount <= loan_amount:
            self.balance +=amount
            self.loan.append(amount)
            return f"You loan request of {amount} has been approved and your balance is {self.balance}"
        else:
            return f"Your loan limit is {loan_amount}"

    
    def repay_loan(self,amount):
        total_loan = sum(self.loan)
        outstanding_balance = total_loan - amount
        
        if amount >= total_loan:
            self.loan.append(amount)
            self.balance -=amount
            return f"Your loan is fully settled "
        
        else:        
            return f"Your outstanding balance is {outstanding_balance}"


    def view_account_details(self):        
        return (f"Account Holder: {self.name} your balance is {self.balance} your outstanding loan is {self.loan}")

    
    def change_account_owner(self,new_name):
        self.name = new_name 
        return f"{new_name} you are now the new account"


    def account_statement(self):
        print (f"{self.name} your account balance is {self.balance}") 
        for deposit in self.deposits:
            print(f"Debits: {deposit}")

        for withdrawal in self.withdrawal:
            print(f"Credits: {withdrawal}")

        

    def interest_calculation(self,amount):
        interest = amount * 0.5
        payable_amount = interest + amount
        return f"If you take a loan of {amount} your interst will be {interest} and your total payable amount is {payable_amount}"

    

    def freeze(self):
        if self.is_frozen == True:
            return f"Your account is frozen cannot perform any transaction due to security reasons"
        elif self.is_frozen != True:
            return f"Your account is not frozen"   


    def close_account(self,name):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawal = []
        self.loan = []        
        return f"Hi {self.name}, Your account is closed"
    
        




   