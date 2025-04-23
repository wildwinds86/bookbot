from stats import *

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    sorted_chars = sort_characters(count_characters(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for x in sorted_chars:
        if x["char"].isalpha():
            print(f"{x["char"]}: {x["num"]}")

    print("============= END ===============")
    

main()