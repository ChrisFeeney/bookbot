import sys
if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words
from stats import get_num_char
from stats import construct_dict
from stats import sort_on

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    file_contents=get_book_text(file_path)
    get_num_words(file_contents)
    chars_dict = get_num_char(file_contents)
    print("--------- Character Count -------")
    chars_list = construct_dict(chars_dict)
    chars_list.sort(reverse=True, key=sort_on)
    #print(chars_list)
    for item in chars_list:
        if f"{item['char']}".isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    #print(chars_dict)
    #print(chars_list)

main()

