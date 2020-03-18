# інтераткивний підруОснови Python. Контрольні завдання 3

def func(var_a, var_b):
    '''compares "var_a" and "var_b". returns ">" "=" "<" or "str"
    '''
    if type(var_a) == str or type(var_b) == str:
        return 'str'
    if var_a > var_b :
        return '>'
    elif var_a == var_b:
        return '='
    elif var_a < var_b:
        return '<'

def count_holes(value):
    '''returns an integer - the number of “holes” in the record of this number, or the string 'error' if the argument passed does not satisfy the requirements: the number is not an integer or is not a number at all. Zeros at the beginning of the recording of a number are not taken into account, if any
    '''
    try:
        int(value)
    except:
        return 'error'
    count_h = 0
    for item in str(int(value)):
        if item in '4690':
            count_h += 1
        elif item == '8':
            count_h += 2
    if count_h == 0:
        return 'error'
    return count_h

def hangman(word, letters):
    '''The function replaces the letters in the string "word" with the underscore character "_", if they are not in the list of "letters" and returns the modified string'''
    new_word = ''
    for item in word:
        if item in letters:
            new_word += item
        else:
            new_word += ' _ '
    return new_word.strip()

print(func('2',3))
print(func(333,434))
print(func.__doc__)

print('0023 >> ', count_holes('0023'))
print('08824 >> ', count_holes('08824'))
print('00abc >> ', count_holes('00abc'))
print(count_holes.__doc__)

print(hangman('python', ['a', 'r', 'y', 'i', 'o']))
print(hangman.__doc__)