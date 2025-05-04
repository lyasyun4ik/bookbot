def get_num_words(book):
    return len(book.split())

"""
This is a badly written code because it is very inefficient. Instead of going through the book one time as in the function below,
it goes through the whole book for each character.

def count_char(book):
    book_lower = book.lower()
    char_count = {}
    for char in book_lower:
        char_count[char] = book_lower.count(char)
    return char_count
"""

def count_char(book):
    chars = {}
    for c in book:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict_list = []
    for char, v in dict.items():
        dict_list.append({"char": char, "num": v})
        dict_list.sort(reverse=True, key=sort_on)
    return dict_list
