import accounthelper


menu =  """
======WELCOME TO SAMMY BANK N.G=========
---------------------------------------
1. Create Account
2. check Balance
3. Deposit
4. Transfer to Another Account
0. Exit
=========================================
"""
while True:
    option = int(input(f"{menu}Enter option: "))
    match option:
        case 1: accounthelper.create_account()
        case 2: accounthelper.check_balance()
        case 3: accounthelper.deposit_fund()
        case 4: accounthelper.transfer_fund()
        case 0: break
print("Thank you for Banking with us")



