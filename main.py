def main():
    
    path = "frankenstein.txt"
    book_contents = get_book_contents(path)

    word_count = count_words(book_contents)
    character_appearances = count_character_appearances(book_contents)
    print_report(path, word_count, character_appearances)
    

def get_book_contents(path):
    
    with open(f"books/{path}") as book:
        return book.read()

def count_words(book_contents):
    split_words = str.split(book_contents)
    return len(split_words)

def count_character_appearances(book_contents):
    
    char_dict = {}

    #Want count to be case independent
    modified_contents = book_contents.lower()

    for char in modified_contents:

        #Filter non-alphabetical characters
        if char.isalpha() == False: continue
        elif char in char_dict: char_dict[char] += 1
        else: char_dict[char] = 1 
    
    return char_dict

def print_report(path, word_count, character_appearances):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    #Sort Dictionary by character regularity
    sorted_dictionary = dict(sorted(character_appearances.items(), key=lambda x:x[1], reverse=True))

    for char in sorted_dictionary:
        print(f"The '{char}' character was found {sorted_dictionary[char]} times")

    print("--- End report ---")

#Intended to be run from root of bookbot repository
main()