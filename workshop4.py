"""
Logan Hall
1/14/23
Workshop 4 Submission
info.tech.logan@gmail.com
"""


"""Task 1"""


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):  # Task 2
        self.name = name

    def change_pin(self, pin):  # Task 2
        self.pin = pin

    def change_password(self, password):  # Task 2
        self.password = password


"""Task 3"""


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.name = name
        self.pin = pin
        self.password = password
        self.balance = 0

    def show_balance(self):  # Task 4
        print("\nHi, " + self.name +
              ". Your current balance is: +" + str(self.balance))

    def withdraw(self):  # Task 4
        withdraw = input(
            "\nHow much would you like to withdraw, " + self.name + ": $")
        try:  # Bonus Task 1 and 2
            int(withdraw)
        except:
            print("Please enter a valid number.")
            self.withdraw()
        else:
            if int(withdraw) > 0:
                withdraw = int(withdraw)
                if (self.balance - withdraw) >= 0:
                    self.balance -= withdraw
                    print("Your new balance is: $" + str(self.balance))
                else:
                    print(
                        "--Sorry, that would cause an overdraft. Withdrawal cancelled.--")
            else:
                print("Please enter a positive number.")
                self.withdraw()

    def deposit(self):  # Task 4
        deposit = input(
            "\nHow much would you like to deposit, " + self.name + ": $")
        try:  # Bonus Task 1 and 2
            int(deposit)
        except:
            print("Please enter a valid number.")
            self.deposit()
        else:
            if int(deposit) > 0:
                deposit = int(deposit)
                self.balance += deposit
                print("Your new balance is: $" + str(self.balance))
            else:
                print("Please enter a number more than $0 to deposit")
                self.deposit()

    def transfer_money(self, other_user):  # Task 5
        transferring_user_pin = int(
            input("\nAuthentication Required.\nPlease enter your PIN, " + self.name + ": "))
        if transferring_user_pin == self.pin:
            print("Transfer authorized.")
            while True:
                transfer_amt = input(
                    "How much would you like to transfer to " + other_user.name + ": $")
                try:  # Bonus Task 1 and 2
                    int(transfer_amt)
                except:
                    print("Please enter a valid number.")
                    # self.transfer_money(other_user)
                else:
                    transfer_amt = int(transfer_amt)
                    if transfer_amt < self.balance:
                        self.balance -= transfer_amt
                        other_user.balance += transfer_amt
                        print("$" + str(transfer_amt) +
                              " transferred from your account.")
                        return True
                    else:
                        print(
                            "Invalid amount. Please enter a number more than $0, and less than your current account balance, to transfer.")
        else:
            print("--Invalid PIN entered. Cancelling transfer.--")
            return False

    def request_money(self, other_user):  # Task 5
        requesting_user_pin = int(
            input("\nAuthentication Required.\nPlease enter the PIN of the user you are requesting money from: "))
        if requesting_user_pin == other_user.pin:
            print("Request authorized.")
            while True:
                request_amt = input(
                    "How much would you like to request from " + other_user.name + ": ")
                try:  # Bonus Task 1 and 2
                    int(request_amt)
                except:
                    print("Please enter a valid number.")
                else:
                    request_amt = int(request_amt)
                    if request_amt < other_user.balance:
                        self.balance += request_amt
                        other_user.balance -= request_amt
                        print("$" + str(request_amt) +
                              " transferred to your account.")
                        break
                    else:
                        print(
                            "Invalid amount. Please enter a number more than $0, or less than the other account's balance, to request.")
        else:
            print("\n--Invalid PIN. Request denied.--")


""" Driver Code for Task 1 """
# user_info = User("Bob", 1234, "password")
# print(user_info.name, user_info.pin, user_info.password)

""" Driver Code for Task 2 """
# user_info = User("Bob", 1234, "password")
# print(user_info.name, user_info.pin, user_info.password)
# user_info.change_name("Robert")
# user_info.change_pin(4321)
# user_info.change_password("drowssap")
# print(user_info.name, user_info.pin, user_info.password)

""" Driver Code for Task 3 """
# bank_user_info = BankUser("Bob", 1234, "password")
# print(bank_user_info.name, bank_user_info.pin, bank_user_info.password, bank_user_info.balance)

""" Driver Code for Task 4 """
# bank_user_info = BankUser("Bob", 1234, "password")
# bank_user_info.show_balance()
# bank_user_info.deposit()
# bank_user_info.show_balance()
# bank_user_info.withdraw()
# bank_user_info.show_balance()

""" Driver Code for Task 5 """
# bank_user_info = BankUser("Bob", 1234, "password")
# bank_user2_info = BankUser("Jim", 4321, "drowssap")
# bank_user2_info.deposit()
# bank_user2_info.show_balance()
# bank_user2_info.withdraw()
# bank_user_info.show_balance()
# transfer_status = bank_user2_info.transfer_money(bank_user_info)
# bank_user2_info.show_balance()
# bank_user_info.show_balance()
# if transfer_status is True:
#     bank_user2_info.request_money(bank_user_info)
# else:
#     print("Transfer was unsuccessful.")
# bank_user2_info.show_balance()
# bank_user_info.show_balance()
