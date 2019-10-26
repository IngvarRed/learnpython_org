
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