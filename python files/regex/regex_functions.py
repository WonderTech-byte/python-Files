import re


def get_all_words_with_vowel_using_regex(sentence):
    pattern = r"[aeiouAEIOU]"
    words = [word for word in sentence.split() if re.findall(pattern, word)]
    return words

def get_word_and_numbers_of_vowel(sentence):
    pattern = r"[aeiouAEIOU]"
    values = [words for words in sentence.split() if re.findall(pattern, words)]
    dictionary = {len(re.findall(pattern, key)): [value for value in values if len(re.findall(pattern, value)) ==len(re.findall(pattern, key))]
                  for key in get_all_words_with_vowel_using_regex(sentence)}

    return dictionary




def is_contains_vowels(sentence):
    pattern = r"[a-zA-Z-0-9]"
    return bool(re.search(pattern, sentence))

print(get_word_and_numbers_of_vowel(" I LOVE EOB"))
