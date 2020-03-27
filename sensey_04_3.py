#
def find_most_frequent(text):
    '''returns the list of lowercase words that are most often found in the text, in alphabetical order'''
    import string

    for symbol in string.punctuation:
        text = text.replace(symbol, '')
    word_dict = {}
    for item in text.lower().split():
        word_dict[item] = text.lower().count(item)
    ret_list = []
    new_dict = {k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)} # How do I sort a dictionary by value?
    print(new_dict)
    for wrd in sorted(word_dict):
        if word_dict[wrd] > 1:
            ret_list.append(wrd)

    return ret_list


print(find_most_frequent('to understand recursion you need first to understand recursion...'))
