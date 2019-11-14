def checkio(number: int) -> int:
    st_number = str(number)
    mult = 1
    for st in st_number:
        if st != '0':
            mult = mult * int(st)
    return mult


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
'''
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
'''
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)