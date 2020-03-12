# Non-unique Elements
''' remove all unique elements (elements which are contained in a given list only once) '''

def checkio(data: list) -> list:
    ''' remove all unique elements (elements which are contained in a given list only once) '''

    new_data = []
    for i in range(len(data)):
        if data.count(data[i]) > 1:
            new_data.append(data[i])

    return new_data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    '''
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
    
    '''
