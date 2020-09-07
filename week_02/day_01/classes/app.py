from modules._bank_account import *

bank_account = BankAccount("John", 500, "business")
bank_account_personal = BankAccount("David", 100, "personal")

print(bank_account.holder_name)
print(bank_account_personal.holder_name)

bank_account.holder_name = "Ada"
print(bank_account.holder_name)

bank_account.pay_in(50)
print(bank_account.balance)

bank_account.pay_monthly_fee()
print(bank_account.balance)

bank_account_personal.pay_monthly_fee()
print(bank_account_personal.balance)