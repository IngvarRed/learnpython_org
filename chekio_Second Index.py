# Second Index

'''
You are given two strings and you have to find an index of the second occurrence of the second string in the first one.

Let's go through the first example where you need to find the second occurrence of "s" in a word "sims".
It’s easy to find its first occurrence with a function index or find which will point out that "s" is the first symbol in a word "sims" and therefore the index of the first occurrence is 0.
But we have to find the second "s" which is 4th in a row and that means that the index of the second occurrence (and the answer to a question) is 3.

Input: Two strings.
Output: Int or None

Example:
second_index("sims", "s") == 3
second_index("find the river", "e") == 12
second_index("hi", " ") is None
'''

def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    indx = None
    num = 0
    for nmr, item in enumerate(text):
        if item == symbol:
            num += 1
            if (item == symbol) and (num == 2):
                indx = nmr
                return indx
    return indx


if __name__ == '__main__':
    print('Example:')
    print(second_index("hi mr Mayor", " "))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')


# other solution

def second_index(text: str, symbol: str) -> [int, None]:
    try:
        return text.index(symbol, text.index(symbol) + 1)
    except ValueError:
        return None


# other solution

def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    result = text.find(symbol, text.find(symbol)+1)
    return result if result != -1 else None