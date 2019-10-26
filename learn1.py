# This prints out "John is 23 years old."
name = "John"
name1 = "Dave"
age = 23
print("%s and %s is %d years old." % (name, name1, age))


# Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $ %s"
print(format_string % data)

# That prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.
astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))

# That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character.
# Notice how there are actually two o's in the phrase - this method only recognizes the first.
astring = "Hello world!"
print(astring.index("o"))

# This counts the number of l's in the string. Therefore, it should print 3.
astring = "Hello world!"
print(astring.count("l"))

#This prints a slice of the string, starting at index 3, and ending at index 6.
# But why 6 and not 7? Again, most programming languages do this - it makes doing math inside those brackets easier.
astring = "Hello world!"
print(astring[3:7])

#This prints the characters of string from 3 to 7 skipping one character.
# This is extended slice syntax. The general form is [start:stop:step].
astring = "Hello world!"
print(astring[3:7:2])

# Note that both of them produce same output
astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

# There is no function like strrev in C to reverse a string.
# But with the above mentioned type of slice syntax you can easily reverse a string like this
astring = "Hello world!"
print(astring[::-1])

# These make a new string with all letters converted to uppercase and lowercase, respectively.
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

# This is used to determine whether the string starts with something or ends with something, respectively.
# The first one will print True, as the string starts with "Hello".
# The second one will print False, as the string certainly does not end with "asdfasdfasdf".
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# This splits the string into a bunch of strings grouped together in a list.
# Since this example splits at a space, the first item in the list will be "Hello", and the second will be "world!".
astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)


# Exercise
# Try to fix the code to print out the correct information by changing the string.
print("Exercise")
print("Try to fix the code to print out the correct information by changing the string.")
# s = "Hey there! what should this string be?"
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))
# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))
# Number of a's should be 2
print("a occurs %d times" % s.count("a"))
# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())
# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())
# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))


# парні \ непарні

some_a = 111
if int(some_a) % 2 == 0:
    print("число А парне =", some_a)
else:
    print("число А непарне =", some_a)


# Loops

# Exercise
# Loop through and print out all even numbers from the numbers list in the same order they are received.
# Don't print any numbers that come after 237 in the sequence.
#
# Прокрутіть і роздрукуйте всі парні номери зі списку номерів у тому ж порядку, в якому вони отримані.
# Не друкуйте будь-які номери, які послідують після 237.
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)

# Loops
# varriant 2
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
for number in numbers:
    if number == 237:
        break

    if int(number) % 2 != 0:
        print(number)

# Functions

# How do you call functions in Python?
# Simply write the function's name followed by (), placing any required arguments within the brackets.
# For example, lets call the functions written above (in the previous example):

# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print(x)

# Exercise
# In this exercise you'll use an existing function, and while adding your own to create a fully functional program.
# Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"
# Run and see all the functions work together!

# У цьому вправі ви будете використовувати існуючу функцію, а також додавати власну, щоб створити цілком функціональну програму.
# Додайте функцію з назвою, list_benefits()яка повертає наступний список рядків: "Більш організований код", "Більше читабельний код", "Просте повторне використання коду", "Дозволити програмістам спільно розділяти та підключатися"
# Додайте функцію з назвою, build_sentence(info)яка отримує один арґумент, що містить рядок, і повертає пропозицію, починаючи з заданої рядки, і закінчуючи рядком "є перевагою функцій!"
# Запустіть і побачите всі функції працюють разом!

# Modify this function to return a list of strings as defined above
def list_benefits():
    benefits = ["More organized code", "More readable code", "Easier code reuse",
                     "Allowing programmers to share and connect code together"]
    return benefits


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    setence = benefit + " is a benefit of functions!"
    return setence


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()



# Classes and Objects

# Accessing Object Variables

# You can create multiple different objects that are of the same class(have the same variables and functions defined).
# However, each object contains independent copies of the variables defined in the class.
# For instance, if we were to define another object with the "MyClass" class and then change the string in the variable above:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# Accessing Object Functions

# To access a function inside of an object you use notation similar to accessing a variable:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()


# Exercise
# We have a class defined for vehicles.
# Create two new vehicles called car1 and car2.
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
#
# У нас є клас, визначений для транспортних засобів.
# Створіть два нових автомобілі під назвою car1 і car2.
# Встановити car1 бути червоним конвертованим вартістю $ 60,000.00 з ім'ям Fer, а car2 - блакитною ванною на ім'я Jump, вартістю $ 10,000.00.

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
# car1
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00
# car2
car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00
# test code
print(car1.description())
print(car2.description())

