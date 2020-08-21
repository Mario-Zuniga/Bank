import Bank

def main():
    # We create the classes
    savings_account = Bank.SavingsAccount(100)
    checking_account = Bank.CheckingAccount(500)

    # The current balance of each class is shown
    print("Savings account: $", savings_account.get_balance())
    print("Checking account: $", checking_account.get_balance())

    print("\n")

    print("Amount to transfer: $120")
    # Using the savings_account we call the transfer method and add the checking_account
    # to validate if it's possible prior to moving the money
    savings_account.transfer(checking_account, 120)

    print("\n")

    # The new balance of each account is printed
    print("Savings account: $", savings_account.get_balance())
    print("Checking account: $", checking_account.get_balance())


# The main function is called to be executed
main()
