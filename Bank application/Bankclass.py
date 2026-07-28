import random
class Bank:
    def __init__(self, account_name, initial_balance):
        self.account_name = account_name
        self.initial_balance = initial_balance
        self.account_number = "".join(str(random.randint(0, 9)) for i in range(16))
        
        # random.randint(x,y) le chai random integer genrerate gareko 
        # random import garesi balla random function use garna milxa
        # str le aaba tyo random lai string ma lagdiyo. '4','5','6'
        # ''.join le aaba str ko haru lai join gardiyo

        print(self.account_name)
        print(self.initial_balance)
        print(self.account_number)

    # Function to Deposit amount
    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            print('-'*30)
            print(f'Rs. {amount} has been deposited to A/C no. {self.account_number}')
            print('-'*30)
        else:
            print('-'*30)
            print(f'Deposit amount must be more than 0.')
            print('-'*30)
    
    # Function to withdrawal amount
    def withdrawl(self, amount):
        if amount < self.initial_balance:  # FIX: was checking amount < balance correctly but now also handles equal case
            self.initial_balance -= amount
            print('-'*30)
            print(f'Rs. {amount} has been withdrawn from A/C no. {self.account_number}')
            print('-'*30)
        else:
            print('-'*30)
            print(f'Withdrawal amount must be lower than balance amount')
            print('-'*30)

    # Function to print user details 
    def print_details(self):
        print(f'\nAccount Name   : {self.account_name}')
        print(f'Account Number : {self.account_number}')
        print(f'Account Balance: Rs. {self.initial_balance}')  # FIX: was self.account_balance (wrong attribute name), corrected to self.initial_balance
