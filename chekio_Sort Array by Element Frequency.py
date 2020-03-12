# Sort Array by Element Frequency
''' Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable. '''

def frequency_sort(items):
    '''
    Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements.
    If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
    '''
    frqn_item = []
    for j, item in enumerate(items):
        frqn_item[j]=(item, items.count(item))
    print(frqn_item)

    return None



if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

'''
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    '''
