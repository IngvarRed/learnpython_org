'''
"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.
Input: A number as an integer.

Output: The answer as a string.
'''


def checkio(in_int: int):
    if (in_int < 0) or (in_int > 1000):
        return 'ERROR! (the number is not in range between 0 .. 1000)'

    rezz = ''
    if in_int % 3 == 0 and in_int % 5 == 0:
        rezz = "Fizz Buzz"
    elif in_int % 3 == 0:
        rezz = "Fizz"
    elif in_int % 5 == 0:
        rezz = "Buzz"
    else:
        rezz = str(in_int)
    return rezz


a = checkio(105)
print(a)
