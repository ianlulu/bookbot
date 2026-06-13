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

def sort_on_d(items: CharacterCount) -> int:
    return items["num"] # for old lesson that does it by dictionary rather than tuple

def sort_on(char_tuple: tuple[str, int]) -> int:
    return char_tuple[1]

def dict_sort(dict):
    dict_list = []

    for key, value in dict.items():
        entry = {"char": key, "num": value}
        dict_list.append(entry)

    dict_list.sort(reverse=True, key=sort_on_d)

    return dict_list

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    empty_list = []

    for char, count in chars_dict.items():
        char_tuple = (char, count)
        empty_list.append(char_tuple)

    sorted_list = sorted(empty_list, key=sort_on, reverse=True)

    return sorted_list
