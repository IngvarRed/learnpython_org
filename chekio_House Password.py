# House Password

'''
The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.
The password contains only ASCII latin letters or digits.
Input: A password as a string.
Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
'''


def checkio(data: str) -> bool:
    if not 9 < len(data) <= 64:
        return False
    uppr = dgt = lwr = False

    for itm in data:
        if itm.isupper():
            uppr = True
        elif itm.isdigit():
            dgt = True
        elif itm.islower():
            lwr = True

    return uppr and dgt and lwr


# Some hints
# Just check all conditions
print(checkio('A1213poklsa'))

'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
'''

# other Solution
def checkio(data: str) -> bool:

    if len(data) >= 10 and any(map(str.isupper, data)) and any(map(str.islower, data)) and any(map(str.isdigit, data)):
        return True
    else:
        return False

# other Solution
def checkio(data: str) -> bool:
    # replace this for solution
    if len(
            data) >= 10 and data.isalnum() == True and data.isalpha() == False and data.isdigit() == False and data.islower() == False and data.isupper() == False:
        return True

    return False