
def format_number_to_million(number):
    print(f"{number:,}")

def format_number_to_hundred(number):
    print(f"{number:.2f}")

def format_number_to_positive(number):
    print(f"+{number}")

def format_number_to_negative_million(number):
    print(f"-{number:,}")

def format_number_to_two_decimal_places(number):
    print(f"{number:.2f}")

def format_number_t0_nearest_whole_number(number):
    print(f"{number:.0f}")

def format_to_currency(number):
    if len(str(number)[2::]) == 3:
        print( str(number)[0::2] +"K")
    else:
        print(number)

def format_to_million(number):
    new_number = number/ 1000000
    print(f"{new_number}K")


word = "hello from here"
print(word.title())
print(word.upper())
print(word.capitalize())
