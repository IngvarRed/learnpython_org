# Flatten a List
def flat_list(array):
    '''Output data: The one-dimensional list with integers'''
    l_array = str(array).replace('[', '').replace(']', '')
    if len(l_array) < 1:
        return []
    new_array = list(l_array.split(','))
    for i, item in enumerate(new_array):
        if item == ' ' :
            del(new_array[i])
        else:
            new_array[i] = int(item)
    return new_array


print(flat_list([-1,[1,[-2,[3],[[5],[10,-11],[1,100,[-1000,[5000]]],[20,-10,[[[]]]]]]]]))

'''
if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
'''

# Other solution
def flat_list(array):
    ret =[]
    for e in array:
        if type(e) == list:
           ret += flat_list(e)
        else:
           ret.append(e)
    return ret

# Other solution. Generator
def flat_list(array):
    for item in array:
        try:
            yield from flat_list(item)
        except TypeError:
            yield item