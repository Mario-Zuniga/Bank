# Parent Class
class BankAccount:

    # We initializa the object with an initial amount of money
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    # Method to deposit
    def deposit(self, amount):
        self.__balance += amount

    # Method to withdraw
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Unavailable funds")
        else:
            self.__balance -= amount

    # Method to obtain the current balance to print it
    def get_balance(self):
        return self.__balance



# Child class
class SavingsAccount(BankAccount):

    # The object is initialized with the init method from the parent class
    def __init__(self, initial_balance):
        BankAccount.__init__(self, initial_balance)

    # The method transfer will grab another account, in the main file is the checking_account
    # and will validate that it has enough money inside to transfer to the savings_account
    def transfer(self, other_account, amount):

        # The balance of the other account is called to verify that the transfer can be done
        if amount > other_account.get_balance():
            # If it can't we notify the user
            print("Unavailable funds in second account")
        else:
            # If it can, we call the methods from the parent account to each child class
            other_account.withdraw(amount)
            self.deposit(amount)


# Child class
class CheckingAccount(BankAccount):

    # The object is initialized with the init method from the parent class
    def __init__(self, initial_balance):
        BankAccount.__init__(self, initial_balance)

    # For the specifc reason of this work, this class will need the methods declared in the parent
    # class, so it will only need the __init__ method
