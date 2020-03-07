# The Most Wanted Letter


def checkio(text: str) -> str:
    import string
    letters = text.lower()
    max_letter = 0
    letter_m = ''
    str_arr = string.ascii_lowercase
    for item in str_arr:
        if letters.count(item) > max_letter :
            max_letter = letters.count(item)
            letter_m = item

    return letter_m




if __name__ == '__main__':
    print("Example:")
    print(checkio("The local tests are done."))

'''
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
'''