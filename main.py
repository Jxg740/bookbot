from stats import get_num_words, get_num_char

def main():    
    # Sets the path to the text
    book_path = "books/frankenstein.txt" 

    # Calls get_book_text with book_path as parameter
    text = get_book_text(book_path)

    # Calls get_num_words from stats with text as parameter
    # Creates a variable to store it
    num_words = get_num_words(text)

    # feeds text to get_num_char and assigns it to char_count
    char_count = get_num_char(text)

    # Prints the number of words
    print(f"{num_words} words found in the document")
    print(char_count)




def get_book_text(path):
    # Takes path as parameter
    with open(path) as f:
         return f.read()
        
main()