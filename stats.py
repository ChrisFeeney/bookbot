def get_num_words(file_contents):
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    print(f"Found {count} total words")

def get_num_char(file_contents):
    characters_dict = {}
    chars_lower = file_contents.lower()
    chars = list(chars_lower)
    for char in chars:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict.update({char: 1})
    return characters_dict

def construct_dict(characters_dict):
    character_list = [{'char':k, 'num':v} for k, v in characters_dict.items()]
    return character_list


def sort_on(items):
    return items['num']



