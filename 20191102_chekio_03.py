def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here
    result = elements[0], elements[2], elements[-2]
    return result


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
    print(easy_unpack((6, 3, 7)))
'''
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
'''
print("\n next\n", "*" * 30)


def index_power(array: list, n: int) -> int:
    """
        Find Nth power of the element with index N.
    """
    if (n in range(len(array))):
        return array[n]**n
    return -1


if __name__ == '__main__':
    print('Example:')
    print(index_power([0, 1], 3))

    # These "asserts" using only for self-checking and not necessary for auto-testing
'''
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
'''