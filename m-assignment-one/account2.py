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
                    
            transaction = Transaction(current_date,amount,narration,"Debits")
            self.transaction.append(transaction)
            self._balance += amount   

            print(f"Hello {self.name} you have {narration} {amount} your new balance is {self._balance} on {transaction.date}")


    def get_withdraw(self,amount,narration = "withdrawals"):
        current_date = datetime.datetime.now()
        if amount > self._balance:
            return "insufficient balance"
        if self._balance-amount < self.minimum_balance:
            return "Can not withdraw,amount is more than minimun balance"
        self._balance -= amount
        transaction = Transaction(current_date,narration,"debits",amount)
        self.transactions.append(transaction)
        print(f"Withdraw:{amount}:New balance {self._balance} on {transaction.date}")    
        

   

   def transfer_funds(self,amount,other_account, narration = "transfer"):
        current_date = datetime.datetime.now()
        if self.is_frozen :
            return "Account is frozen,your can not transfer money"
        if amount > self._balance:
            return 'insufficient balance for transfer'
        self.withdraw(amount)
        other_account.deposit(amount)
        self._balance -= amount
        transaction = Transaction(current_date,narration,"debits",amount)
        self.transactions.append(transaction)
        return f'You have transferred {amount} to {other_account.name} :New balance {self._balance} on {transaction.date}'



    def request_loan(self,amount,narration = "requested_loan"):
        current_date = datetime.datetime.now()
        if self.is_frozen :
            return "Account is frozen,your can not transfer money"
        if amount <= 0:
            return "You don't have enough amount in your account"
        self.loan_amount+=amount
        self._balance += amount
        transaction = Transaction(current_date,narration,"loan",amount)
        self.transactions.append(transaction)
        return f'Loan requested:{amount}.New balance:{self._balance}'



    def repay_loan(self,amount,narration = "repay_loan"):
        excess_money = self.loan_amount - amount
        if amount <= 0:
            return "You don't have enough amount in your account"
        if amount < self.loan_amount:
            return 'Can not pay more than the loan amount'
        excess_money += amount
        self._balance -= amount
        self.loan_amount -= amount
        transaction = Transaction(current_date,narration,"repaid_loan",amount)
        self.transactions.append(transaction)
        return f"You repaid:{amount}.Remaining amount:{self.loan_amount}"


        
    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "credit":
                balance += transaction.amount
            elif transaction.transaction_type == "debits":
                balance -= transaction.amount
            elif transaction.transaction_type == "debits":
                balance -= transaction.amount
            elif transaction.transaction_type == "loan":
                balance+= transaction.amount
            else: transaction.transaction_type == "repay_loan"
            balance -= amount
        return balance


    def show_balance(self):
        return f"current balance:{self.get_balance()}"


    def account_details(self):
        return f"Account owner:{self.name}.current balance:{self._balance}.Loan amount:{self.loan_amount}"


    def change_account_owner(self, new_owner):
        self.owner = new_owner
        return f"Account owner changed to: {self.owner}"


    def transaction_history(self):
        return self.transactions


    def interest_calculation (self):
        interest = self._balance * 0.05
        self._balance += interest
        self.transactions.append(interest)
        return f"interest {interest}.New balance:{self._balance}"


    def freeze_account(self):
        self.is_frozen = True
        return 'Account is locked'


    def unfreeze_account (self):
        self.is_frozen = False
        return "Account has been unfrozen"


    def set_minimum_balance (self):
        if amount <= 0:
            return "minimum value must be positive numbers"
        self.minimum_balance = 200
        return f"minimum balance set to:{self.minimun_balance}
"

    def close_account(self):
        self._balance = 0
        self.transactions.clear()
        return "Account closed"
