class Mario():
    """
    16. Imagine you are creating a Super Mario game. You need to define a
    class to represent Mario. What would it look like? If you aren't familiar
    with SuperMario, use your own favorite video or board game to model
    a player.
    """
    def hat(self):
        print("This is mario's hat.")

    def eyes(self):
        print("This is mario's eyes.")

    def arms(self):
        print("This is mario's arms.")

    def legs(self):
        print("This is mario's legs.")

    def moustache(self):
        print("This is mario's moustache.")


class User():
    """
    15. Imagine you are designing a banking application. What would a
    customer look like? What attributes would she have? What methods
    would she have?
    """
    def __init__(self, username, account_no, available_bal):
        self.username = username
        self.account_no = account_no
        self.available_bal = available_bal

    def available_balance(self):
        available_bal = self.available_bal
        return available_bal

    def withdraw_money(self):
        if self.available_bal:
            return "You can withdraw money"
        else:
            return "Balance not sufficient"

    def deposite_money(self, amount):
        self.available_bal += amount
        return "Amount deposited sucessfully"

    def account_info(self):
        print("Username", self.username)
        print("Account_number: ", self.account_no)
        print("Available Balance: ", self.available_bal)
