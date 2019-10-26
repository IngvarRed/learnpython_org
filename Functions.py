# Functions

# Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. For example:
def my_function():
    print("Hello From My Function!")

# Functions may also receive arguments (variables passed from the caller to the function). For example:
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

# Functions may return a value to the caller, using the keyword- 'return' . For example:
def sum_two_numbers(a, b):
    return a + b

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

