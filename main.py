from stats import count_words

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    word_count = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{word_count} words found in the document")

main()