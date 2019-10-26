# Basic String Operations

# Strings are bits of text. They can be defined as anything between quotes:

astring = "Hello world!"
astring2 = 'Hello world!'

# That prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.

astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))

# That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character.
# Notice how there are actually two o's in the phrase - this method only recognizes the first.

astring = "Hello world!"
print(astring.index("o"))

# For those of you using silly fonts, that is a lowercase L, not a number one.
# This counts the number of l's in the string. Therefore, it should print 3.

astring = "Hello world!"
print(astring.count("l"))

# This prints a slice of the string, starting at index 3, and ending at index 6. But why 6 and not 7?
# Again, most programming languages do this - it makes doing math inside those brackets easier.

astring = "Hello world!"
print(astring[3:7])

# This prints the characters of string from 3 to 7 skipping one character.
# This is extended slice syntax. The general form is [start:stop:step].

astring = "Hello world!"
print(astring[3:7:2])

# This prints the characters of string from 3 to 7 skipping one character.
# This is extended slice syntax. The general form is [start:stop:step].

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

#vThere is no function like strrev in C to reverse a string.
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
