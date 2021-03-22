class Customer:

    def __init__(self, name, bank_account_number, pin):
        self.name = name
        self.bank_account_number = bank_account_number
        self.pin = pin

    def get_name(self):
        return self.name

    def get_bank_account_number(self):
        return self.bank_account_number

    def get_pin(self):
        return self.pin
