from functools import reduce


def add_to_tuple(numbers):
    newNumber  = list(numbers)
    newNumber.append(700)
    return tuple(newNumber)

def add_to_tuples_of_numbers(numbers):
    new_number = list(numbers)
    new_number[2][1] = 99
    return new_number

# fruits = ('apple', 'banana', 'cherry')
def add_to_tuples_of_fruits(fruits):
    new_fruits = list(fruits)
    new_fruits.append('mango')
    return tuple(new_fruits)

# numbers = (10, 20, 30, 40)
def unpacking_numbers(numbers):
    first_number, second_number, *others = numbers
    print(others)

#2D LIST TASKS

def summation_of_2d_list(numbers):
    return [sum(number) for number in numbers]
#
# def index_0f(two_d_list):
#     for outer_index in range(len(two_d_list)):
#         for index, inner_list in enumerate(two_d_list):
#             inner_list[index] =


# FILTER ASSIGNMENT
def is_even(number):
    return number % 2 == 0

def length_greater_than_5(word):
    return len(word) > 5

def first_element_greater_than_2(inner_list):
    number, letter =inner_list
    return number > 2

def number_divisible_by_3_and_5(number):
    return number % 3 == 0 and number % 5 == 0

def is_palindrome(word):
    return word == word[::-1]

def is_greater_than_5(number):
    return number > 5


numbers = [number for number in range(22)]
range_of_numbers  = [number for number in range(51)]
words = ['cat','elephant','tiger','lion','c++']
list_of_numbers = [(1,'A'), (4,'B'), (2,'C')]
check_palindrome = ['Filter', 'level', 'python','madam']
message = ['I', 'LOVE', 'PYTHON']

#
# print(list(filter(is_even,numbers)))
# print(list(filter(length_greater_than_5,words)))
# print(list(filter(first_element_greater_than_2,list_of_numbers)))
# print(list(filter(number_divisible_by_3_and_5,range_of_numbers)))
# print(list(filter(is_palindrome,check_palindrome)))


#MAP
def to_upper_case(word):
    return word.upper()

def to_square(number):
    return number **2

def capitalize_first_case(word):
    return word[0:1].upper() + word[1::]

def plus_10_percent(number):
    return (0.1 * number) + number

#
# print(list(map(to_square, numbers)))
# print(list(map(to_upper_case, words)))
# print(list(map(capitalize_first_case, words)))
# print(list(map(plus_10_percent, numbers)))

#REDUCE
def sum_up(first_number, second_number):
    return first_number + second_number

def max_of(firs_number, second_number):
    return max(firs_number, second_number)

def concat(first_word, other_word):
    return first_word +' '+ other_word

def product_of(first_word, second_word):
    return first_word * second_word

number = [1,2,3,4]


# print(reduce(sum_up, numbers))
# print(reduce(max_of, numbers))
# print(reduce(concat, message))
# print(reduce(product_of,map(to_square,number)))


#OTHERS

number = [(1,2), (3,4), (5,6)]
new_list = summation_of_2d_list(number)


# print(list(filter(is_greater_than_5, new_list)))


number = ['123', '456','789', 'abc', 'def']

def remove_non_numeric(list_of_numbers):
    numerical_list =[int(numerics) for numerics in list_of_numbers if numerics.isdigit()]
    return numerical_list

new_list = remove_non_numeric(number)
sum_of_list = reduce(sum_up, new_list)

# print(sum_of_list)