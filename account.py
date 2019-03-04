"""
A class that performs the basic functionality associated with a bank account.
"""
class Account(object):
    LOWER_LIMIT = 1000
    
    #Constructor
    def __init__(
            self, account_name, account_id, account_pin, account_balance=1000):
        
        #Class Attributes 
        self.account_name = account_name
        self.account_id = account_id
        self.account_pin = account_pin
        self.account_balance = account_balance

    # Suggestion: Instead of having this function carry out the logic of
    # getting user input, why not have this functionality in the bank Class
    # then pass the value to this function and process the value from there.
    # This function could throw an exception if the withdraw_amount is greater
    # than the account_balance.
    
    
    def withdraw(self):
        
        #Withdraws amount from account
        prompt = "Please enter the amount you wish to withdraw: "
        withdraw_amount = int(input(prompt))
        if withdraw_amount > self.account_balance:
            print(
                "Prohibited transaction. Withdrawals in excess of the "
                "account balance are not allowed. Please try again.")
        else:
            self.account_balance -= withdraw_amount
            if self.account_balance < self.LOWER_LIMIT:
                print(
                    "Prohibited transaction. Account balances lower than "
                    "{self.LOWER_LIMIT} are not allowed. Please try again.")
                self.account_balance += withdraw_amount
            else:
                # self.account_balance -= withdraw_amount
                print(
                    "Transaction successful. Your new account balance is "
                    f"{self.account_balance}")

    # Suggestion: Instead of having this function carry out the logic of
    # getting user input, why not have this functionality in the bank Class
    # then pass the value to this function and process the value from there.
    def deposit(self):
        """Deposits money into the account.

        The amount of money that the user wishes to deposit into the
        account is added to the current account balance.
        """
        prompt = "Please enter the amount you wish to deposit: "
        deposit_amount = int(input(prompt))

        self.account_balance += deposit_amount
        print("Transaction successful. Your new account balance is",
              self.account_balance)

    def print_account_balance(self):#get_balance
        """Displays the amount of money currently in the account."""
        print("Your current account balance is: {self.account_balance}")
