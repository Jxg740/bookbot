
def get_num_words(text):
    # Assigns the text parameter to words var and splits it into a list
    words = text.split()
    return len(words)


def get_num_char(text):
    chars = list(text.lower())
    chars_dict = {}
    for char in chars:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


