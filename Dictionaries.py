
# Dictionaries

# For example, a database of phone numbers could be stored using a dictionary like this:

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# Alternatively, a dictionary can be initialized with the same values in the following notation:

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# Iterating over dictionaries

# Dictionaries can be iterated over, just like a list.
# However, a dictionary, unlike a list, does not keep the order of the values stored in it.
# To iterate over key value pairs, use the following syntax:

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Removing a value

# To remove a specified index, use either one of the following notations:

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

# or:

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)


# Exercise

# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook["Jake"] = 938273443
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")