class Balance:
    def __init__(self, checking_balance, savings_balance, brokerage_balance, liabilities_balance):
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        self.brokerage_balance = brokerage_balance
        self.liabilities_balance = liabilities_balance

    # determine the status level of a member
    # tot < 10000 standard member
    # 10001 <= tot < 50000 gold member
    # tot > 50001 premier member
    def real_bank_status(self):
        tot = self.checking_balance + self.savings_balance + self.brokerage_balance - self.liabilities_balance
        bank_status = ()
        if tot < 10000:
            bank_status = "Standard Member"
        elif 10001 <= tot < 50000:
            bank_status = "Gold Member"
        else:
            bank_status = "Premier Member"

        print(f"Thank you for being a {bank_status} at Big Bank Inc.")

    def get_balance_info(self):
        print("Your balances are:")
        print(f"Checking: {self.checking_balance}\nSavings: {self.savings_balance}\nBrokerage: {self.brokerage_balance}\nLiablities -{self.liabilities_balance}")

