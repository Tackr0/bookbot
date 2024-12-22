def main():

    path = "frankenstein.txt"
    book_contents = get_book_contents(path)

    book_word_count = count_words(book_contents)
    print(book_word_count)

def get_book_contents(book_file):
    
    with open("books/frankenstein.txt") as book:
        return book.read()

def count_words(book_contents):
    split_words = str.split(book_contents)
    return len(split_words)

main()

