def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    characters = {}
    for c in book_text.lower():
        if c in characters:
            characters[c] += 1
        else: 
            characters[c] = 1

    return characters

def sort_characters(characters_dict):
    def sort_on(dict):
        return dict["num"]

    sorted_list = []
    for char, num in characters_dict.items():
        sorted_list.append({"char" : char, "num" : num})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list