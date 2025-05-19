
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

# Helper function used for sorting; returns the 'num' value from a dictionary
def sort_on(d):
    return d["num"]

# Function to convert a dictionary of character counts into a sorted list of dictionaries
def sorted_char_list(dict):
    dict_list = []
    # Convert each character and its count into a dictionary and add it to a list
    for i in dict:
        dict_list.append({"char": i, "num": dict[i]})
    # Sort the list of dictionaries in descending order based on the 'num' value
    dict_list.sort(reverse=True, key=sort_on)
     # Return the sorted list
    return dict_list