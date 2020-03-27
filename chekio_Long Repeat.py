def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    if len(line) < 1:
        return 0
    old_item = ''
    count_item = 0
    count_max = 0
    for item in line:
        if item == old_item:
            count_item += 1
            print(item, '>>>', count_item)
        else:
            if count_item > count_max:
                count_max = count_item
                print(item, '>>>', count_item, '>>>', count_max)
            count_item = 1
            old_item = item
    if count_max > count_item:
        return count_max
    return count_item




print(long_repeat('abababab'))

'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
'''
