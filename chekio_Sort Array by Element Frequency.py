# Sort Array by Element Frequency
''' Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable. '''


def frequency_sort(items):
    '''
    Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements.
    If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
    '''

    for i, item_i in enumerate(items):
        for j, item_j in enumerate(items):
            if items.count(item_j) <= items.count(item_i):
                if items[i] != items[j]:
                    (items[i], items[j]) = (items[j], items[i])

    return items


# !!!! That solution !!!
def frequency_sort(items): # sortbyfreq(arr):
    s = set(items)
    keys = {n: (-items.count(n), items.index(n)) for n in s}
    return sorted(items, key=lambda n: keys[n])

# other solution
def frequency_sort(items):
    # group items ordering them by order of appearance
    # this handle the case where 2 different items get same frequency
    a = sorted(items,key=items.index)

    # sor by frequency
    a = sorted(a,key=items.count, reverse=True)

    return a

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
