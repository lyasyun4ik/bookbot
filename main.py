from stats import get_num_words, count_char, sort_dict

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    num_words = get_num_words(book)
    char_dict = count_char(book)
    char_dict_list = sort_dict(char_dict)

    print(f"============ BOOKBOT ============ \n"
f"Analyzing book found at {book_path}...\n"
f"----------- Word Count ----------\n"
f"Found {num_words} total words\n"
f"--------- Character Count -------")
    for item in char_dict_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as b:
        return b.read()

main()