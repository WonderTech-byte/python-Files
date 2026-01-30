import account

def create_account():
    name = input("Enter your name: ")
    while True:
        if not account.validate_name(name):
            name = input("Name must me letters Only: ")
        else:
            break
    phone_number = input("Enter your phone number: ")
    while True:
        if not account.validate_phone_number(phone_number):
            phone_number = input("Number must be digits only and must be 11 digits: ")
        else:
            break
    if not account.fetch_user(phone_number):
        pin = input("Create Pin (4 Digits): ")
        while True:
            if not account.validate_pin(pin):
                pin = input("Pin must be 4 Digits: ")
            else:
                break
        account.create_account(name, phone_number, pin)
        print("Account created successfully!!\n================================")
        print(f"ACCOUNT NAME: {name}\nACCOUNT NO: {phone_number}\nBalance: {0}")
        print("================================")
    else:
        print("User with phone number already exists")


def check_balance():
    phone_number = input("Enter your phone number: ")
    while True:
        if not account.validate_phone_number(phone_number):
            phone_number = input("Number must be digits only and must be 11 digits: ")
        else:
            break
    if account.fetch_user(phone_number):
        pin = input("Enter Pin (4 Digits): ")
        if account.check_pin(phone_number, pin):
            print("================================\n\tACCOUNT BALANCE\n================================")
            print(account.get_user_balance(phone_number))
        else:
            print("Wrong PIN")
    else:
        print("User do not exists")


def deposit_fund():
    phone_number = input("Enter your phone number: ")
    while True:
        if not account.validate_phone_number(phone_number):
            phone_number = input("Number must be digits only and must be 11 digits: ")
        else:
            break
    if account.fetch_user(phone_number):
        amount = int(input("Enter your amount: "))
        if amount > 0:
            account.deposit_money(phone_number, amount)
            pin = input("Enter Pin (4 Digits): ")
            if account.check_pin(phone_number, pin):
                print("\tDeposit successfully!!")
                print("================================\n\tACCOUNT BALANCE\n================================")
                print(account.get_user_balance(phone_number))
            else:
                print("Wrong PIN")
        else:
            print("Cannot deposit negative amount")
    else:
        print("Account do not exists")


def transfer_fund():
    phone_number = input("Enter your phone number: ")
    while True:
        if not account.validate_phone_number(phone_number):
            phone_number = input("Number must be digits only and must be 11 digits: ")
        else:
            break
    if account.fetch_user(phone_number):
        recipient_account = input("Enter recipient account or phone number: ")
        if not recipient_account.startswith('0'):
            recipient_account = "0" + recipient_account
        while True:
            if not account.validate_phone_number(phone_number):
                recipient_account = input("Number must be digits only and must be 11 digits: ")
            else:
                break
        if account.fetch_user(recipient_account):
            amount = int(input("Enter your amount: "))
            if amount > 0:
                pin = input("Enter Pin (4 Digits): ")
                if account.check_pin(phone_number, pin):
                    tranfer_status = account.transfer_money(phone_number, recipient_account, amount)
                    if tranfer_status == "Transfer money successfully!!":
                        print("================================")
                        print(tranfer_status)
                        print("================================\n\tACCOUNT BALANCE\n================================")
                        print(account.get_user_balance(phone_number))

                    else:
                        print(tranfer_status)
                else:
                    print("Wrong PIN")
            else:
                print("Cannot deposit negative amount")
        else:
            print("Recipient do not exists")
    else:
        print("Account do not exists")

