from stats import get_num_words
from stats import char_count, report, sort_characters_by_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        #print(text)
        print("scuess")
        return text

get_book_text(filepath)
#with open(path_to_file) as f:
    #do something with file here
#frank = "books/frankenstein.txt"



#get_num_words(frank)
report(filepath)


