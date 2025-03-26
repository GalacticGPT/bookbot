frank = "books/frankenstein.txt"

def get_num_words(filepath):
    text = get_book_text(filepath)
    print(text)
    words = text.split()
    #print(words)
    #type(words)
    count = len(words)
    print(f'{count} words found in the document')

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        #print(text)
        return text
    
def char_count(filepath):
    chars = {}
    text = get_book_text(filepath)
    for char in text.lower():
        chars[char] = chars.get(char,0) + 1
        #chars.add(char)
    return chars


def report(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    # Word count
    text = get_book_text(filepath)
    words = text.split()
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")

    # Character frequency
    print("--------- Character Count -------")
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1

    sorted_chars = sort_characters_by_count(chars)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


#Two steps, sort out tthe nonnumbers, then sort by frequency

#filtered = char: count for char, count in chars.items() if char.isalpha()


def sort_characters_by_count(char_dict):
    filtered = {
        char:count for char, count in char_dict.items()
        if char.isalpha()
    }
    

#convert to list
    char_list = [{"char": char, "num": count} for char, count in filtered.items()]

    char_list.sort(key = lambda d: d["num"], reverse = True)

    return char_list