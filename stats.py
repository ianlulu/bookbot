from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

def word_count(text):
    words = text.split()
    
    return len(words)

def char_count(book):
    dictionary = {}

    for word in book:
        for char in word:
            c = char.lower()

            if c in dictionary:
                dictionary[c] = dictionary[c] + 1
            else:
                dictionary[c] = 1

    return dictionary

def sort_on(items: CharacterCount) -> int:
    return items["num"]

def dict_sort(dict):
    dict_list = []

    for key, value in dict.items():
        entry = {"char": key, "num": value}
        dict_list.append(entry)

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
