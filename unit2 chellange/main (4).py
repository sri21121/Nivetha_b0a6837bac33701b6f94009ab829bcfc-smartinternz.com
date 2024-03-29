class BankAccount:

  def _init_(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited ${}. New balance:${}".format(amount,
                                                    self.__account_balance))
    else:
      print("Invalid deposit amount. Please deposit a positive  amount.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdrew ${}. New balance: ${}".format(amount,
                                                    self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (account #{}): ${}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


# Create an instance of the BankAccount class
account = BankAccount(account_number="987654321",
                      account_holder_name="Nivi",
                      initial_balance=8000.0)
# Test deposit and withdrawal functionalty
#account.display_balance()
#account.deposit(800.0)
#account.withdraw(200.0)
account.display_balance()
