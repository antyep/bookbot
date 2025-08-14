import sys
from stats import get_num_words
from stats import character_counter
from stats import sort_characters

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    result = character_counter(text)
    character_counts_dictionary = character_counter(text)
    sorted_list = sort_characters(result)
    char_counts_str = ""
    for item in sorted_list:
        char_counts_str += f"{item['char']}: {item['num']}\n"
    print(f"""
    ============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{char_counts_str}
============= END ===============
    """)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)
