
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


def sort_on(d):
    return d["num"]

def sorted_char_list(dict):
    dict_list = []
    for i in dict:
        dict_list.append({"char": i, "num": dict[i]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list