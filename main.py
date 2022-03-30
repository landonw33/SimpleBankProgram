from user import User
from balance import Balance

user_input = int(input("User ID number: "))

bank_member_123 = User("joshh@gmail.com", "Josh Hobs", "pwd123", "1654", "North Ivinson Ave", "Salida", "KS", "67401", 123)
bank_member_123_balances = Balance(1500, 15000, 2200, 800)

bank_member_602 = User("walter2@ymail.com", "Walter White", "ilikechem","308", "Negra Arroya Lane", "Albuquerque", "NM", "87101", 602)
bank_member_602_balances = Balance(1500, 1000, 2200, 1000)

# bank_member_123.user_id is how to access just the user id
# for a much bigger group of users you will probably want a for loop and to put all the info outside of main
if user_input == bank_member_123.user_id:
    print(bank_member_123.user_id)
    print(f"Welcome back {bank_member_123.name}")
    bank_member_123.get_user_info()
    bank_member_123_balances.get_balance_info()
    bank_member_123_balances.real_bank_status()
elif user_input == bank_member_602.user_id:
    print(f"Welcome back {bank_member_602.name}")
    bank_member_602.get_user_info()
    bank_member_602_balances.get_balance_info()
    bank_member_602_balances.real_bank_status()
else:
    print("We could not find your account.")

