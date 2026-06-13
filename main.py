import sys
from stats import word_count, char_count, dict_sort

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file = f.read()

    return file

def main():
    print("============ BOOKBOT ============")

    path = sys.argv[1]

    text = get_book_text(path)

    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")

    num_words = word_count(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    num_chars = char_count(text)
    # print(num_chars)

    num_list = dict_sort(num_chars)
    for i in num_list:
        if i["char"].isalpha() is True:
            print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")


main()
