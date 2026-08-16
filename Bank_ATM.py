class Bank_ATM:

    def __init__(self):
        self.pin = ""
        self.balance = 0

    def menu(self):
        print("1. Enter 1 to set pin")
        print("2. Enter 2 to check balance")
        print("3. Enter 3 to deposit money")
        print("4. Enter 4 to withdraw money")
        print("5. Enter 5 to change pin")
        print("6. Enter 6 to exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                self.setPin()
            case 2:
                self.chack_balance()
            case 3:
                self.deposit_money()
            case 4:
                self.withdraw_money()
            case 5:
                self.change_pin()
            case 6:
                self.exit()

    def setPin(self):
        if self.pin == "":
            self.pin = input("Enter your pin: ")
            print("Pin set successfully:", self.pin)
            self.menu()
        else:
            print("Pin is already set:", self.pin)
            self.menu()

    def chack_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print("Your current balance: ", self.balance)
            self.menu()
        else:
            print("Invalid Pin")
            self.menu()

    def deposit_money(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            deposit = int(input("Enter the amount: "))
            self.balance += deposit
            print("Your current balance: ", self.balance)
            self.menu()
        else:
            print("invalid pin")
            self.menu()

    def withdraw_money(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            withdrawMoney = int(input("Enter withdraw money: "))
            self.balance -= withdrawMoney
            print("Your current balance: ", self.balance)
            self.menu()
        else:
            print("invalid pin")
            self.menu()

    def change_pin(self):
            user_pin = input("Enter your old pin: ")
            if user_pin == self.pin:
                new_pin = input("Enter your new pin: ")
                self.pin = new_pin
                self.menu()
            else:
                print("invalid pin")
                self.menu()
    def exit(self):
        print("Thank You")

obj1 = Bank_ATM()
obj1.menu()