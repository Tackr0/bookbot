def main():

    path = "frankenstein.txt"
    book_contents = get_book_contents(path)

    word_count = count_words(book_contents)
    character_appearances = count_character_appearances(book_contents)
    print(character_appearances)
    

def get_book_contents(book_file):
    
    with open("books/frankenstein.txt") as book:
        return book.read()

def count_words(book_contents):
    split_words = str.split(book_contents)
    return len(split_words)

def count_character_appearances(book_contents):
    
    char_dict = {}

    #Want count to be case independent
    modified_contents = book_contents.lower()

    for char in modified_contents:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1 
    
    return char_dict

main()

