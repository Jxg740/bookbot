from stats import get_num_words, get_num_char, sorted_char_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def main():     

    # Calls get_book_text with book_path as parameter
    text = get_book_text(book_path)

    # Calls get_num_words from stats with text as parameter
    # Creates a variable to store it
    num_words = get_num_words(text)

    # feeds text to get_num_char and assigns it to char_count
    char_count = get_num_char(text)

    
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # Iterates through the sorted_char_list
    for item in sorted_char_list(char_count):
        # verifies that the value of the key "char" is a letter only
        if item["char"].isalpha():
            # prints the value of the keys "char" and "num"
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    



def get_book_text(path):
    # Takes path as parameter
    with open(path) as f:
         return f.read()
        
main()