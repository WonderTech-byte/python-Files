

bank = []
phone_contact = '09072175891'
demo_user1 = {
    "Name": "Samuel Omosefunmi",
    "Account_Number": phone_contact[1::],
    "Balance": 0,
    "Phone_number": phone_contact,
    "Pin": "1234",

}

phone_contact = "09069005518"
demo_user2 = {
    "Name": "Ayobami",
    "Account_Number": phone_contact[1::],
    "Balance": 0,
    "Phone_number": phone_contact,
    "Pin": "4321",

}

demo_user3 = {
    "Name": "Ayobami",
    "Account_Number": phone_contact[1::],
    "Balance": 0,
    "Phone_number": '09072175890',
    "Pin": "4321",

}
# bank.append(demo_user1)
# bank.append(demo_user2)



def create_account(name, phone_contact, pin):
    check_phone_contact = [True for user in bank if user["Phone_number"] == phone_contact ]
    if not check_phone_contact:
        user_profile = {
            "Name": name,
            "Account_Number": phone_contact[1::],
            "Balance": 0,
            "Phone_number": phone_contact,
            "Pin": pin,
        }
        bank.append(user_profile)
        return "Account created successfully....."
    return "Account already exist!!"


def check_pin(phone_number, pin):
    for user in bank:
        if user.get("Phone_number") == phone_number and user.get('Pin') == pin:
            return user
    return False


def fetch_user(phone_number):
    for user in bank:
        if user.get("Phone_number") == phone_number:
            return user
    return False


def validate_phone_number(phone_number):
    import re
    if re.match( r'^\d{11}$', phone_number):
        return True
    return False

def validate_name(name):
    import re
    if re.match('^[A-Za-z ]+$', name):
        return True
    return False

def validate_pin( pin):
    import re
    if re.match(r'^\d{4}$', pin):
        return True
    return False


def get_user_info(phone_number):
    for user in bank:
        if user.get("Phone_number") == phone_number:
            return f"ACCOUNT NAME: {user['Name']} \nACCOUNT NO: {user['Account_Number']}"
    return "Account not found!!"


def get_user_balance(phone_number):
    for user in bank:
        if user.get("Phone_number") == phone_number:
            return f"ACCOUNT NAME: {user['Name']} \nACCOUNT NO: {user['Account_Number']}\nBALANCE: ${user['Balance']}"
    return "Account not found!!"

def deposit_money(phone_number, amount):
    user = fetch_user(phone_number)
    if user is not False and amount> 0:
        user["Balance"] += amount
        return get_user_balance(phone_number)
    return None

def transfer_money(phone_number, recipient_account, amount):
    user = fetch_user(phone_number)
    recipient = fetch_user(recipient_account)
    if not user:
        return "user not found!!"
    if not recipient:
        return "recipient not found!!"
    if user["Phone_number"] != recipient["Phone_number"]:
        if not amount < 0 and user["Balance"] - amount >= 100:
            user["Balance"] -= amount
            recipient["Balance"] += amount
            return "Transfer money successfully!!"
        else:
            return "Account too low to make transfer!!"
    else:
        return "cannot make transfer to your account!!"
    return "Insufficient funds, fund account!!"


