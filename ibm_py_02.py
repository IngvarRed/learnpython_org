"""
Probability Bag

You have been tasked with creating a lab that demonstrates the basics of probability by simulating a bag filled with colored balls. The bag is represented using a dictionary called "bag", where the key represents the color of the ball and the value represents the no of balls. The skeleton code has been made for you, do not add or remove any functions. Complete the following functions -

fillBag - A function that packs it's arguments into a global dictionary "bag".
totalBalls - returns the total no of balls in the bucket
probOf - takes a color (string) as argument and returns probability of drawing the selected ball. Assume total balls are not zero and the color given is a valid key.
probAll - returns a dictionary of all colors and their corresponding probability
"""


def fillBag(**balls):
    '''
    fillBag - A function that packs it's arguments into a global dictionary "bag".
    '''
    global bag
    bag={}
    for color in balls:
        bag[color] = balls[color];
    return


def totalBalls():
    '''
    totalBalls - returns the total no of balls in the bucket
    '''
    return sum(bag.values())


def probOf(color):
    '''
    probOf - takes a color (string) as argument and returns probability of drawing the selected ball. Assume total balls are not zero and the color given is a valid key.
    '''

    return bag[color] / totalBalls();


def probAll():
    '''
    probAll - returns a dictionary of all colors and their corresponding probability
    '''
    probblt = {}
    for color in bag:
        probblt[color] = bag[color] / sum(bag.values());
    return probblt


# alternative Verssion

def fillBag(**balls):
    global bag
    bag = balls

def totalBalls():
    total = 0
    for color in bag:
        total += bag[color]
    return total
    # alternatively,
    # return sum(bag.values())

def probOf(color):
    return bag[color] / totalBalls()

def probAll():
    probDict = {}
    for color in bag:
        probDict[color] = probOf(color)
    return probDict

# end Verssion

# Run this snippet of code to test your solution. Note: This is not a comprehensive test.


testBag = dict(red = 12, blue = 20, green = 14, grey = 10)
total =  sum(testBag.values())
prob={}
for color in testBag:
    prob[color] = testBag[color]/total;

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return ' Test Failed'

print("fillBag : ")
try:
    fillBag(**testBag)
    print(testMsg(bag == testBag))
except NameError as e:
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")

print("totalBalls : ")
try:
    print(testMsg(total == totalBalls()))
except NameError as e:
    print('Error! Code: {c}, Message: {m}'.format(c=type(e).__name__, m=str(e)))
except:
    print("An error occured. Recheck your function")

print("probOf")
try:
    passed = True
    for color in testBag:
        if probOf(color) != prob[color]:
            passed = False

    print(testMsg(passed))
except NameError as e:
    print('Error! Code: {c}, Message: {m}'.format(c=type(e).__name__, m=str(e)))
except:
    print("An error occured. Recheck your function")

print("probAll")

try:
    print(testMsg(probAll() == prob))
except NameError as e:
    print('Error! Code: {c}, Message: {m}'.format(c=type(e).__name__, m=str(e)))
except:
    print("An error occured. Recheck your function")
