

def sum_of_list(numbers):
    return sum(numbers)


def length_of_elements(words):
     new_list = [len(word) for word in words]
     return new_list

def elements_at_odd_indexes(numbers):
    new_list = [number for index, number  in enumerate(numbers,0) if index % 2 == 1]
    return new_list

def sort_and_add(words):
    words.sort()
    new_list = [(index, word, len(word)) for index, word in enumerate(words , 0)]
    return new_list
