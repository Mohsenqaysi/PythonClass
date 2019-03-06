
# Variables and Types

#S we can do it this way as well:
# You can just as easily store a string as a variable and then print it to stdout:

my_string = "Hello, World!"
print(my_string)

# \n => new line 
print("\n\n-------------------- \n\n")

# We can define Strings in two different ways:

my_string = 'This string is using a single quote'
print(my_string)

my_string = "This string is using a double quotes"
print(my_string)

# but why ?
print("\nBut why not one way?\n")

string_with_quote = "Don't forget to flush the toilet !!!"
print(string_with_quote)

# string_with_quote = 'Do't forgot to flush the toilet !!!'
# print(string_with_quote)

print("\n\n--------------------\n\n")

# we can join two or more strings together (concatenating strings)

first_name = "Mark"
last_name = "Dowling"

full_name = first_name + last_name

print(full_name)

print("\nWe have a problem above?\n")

# we need to formate the string ... one simple way is as follow:

full_name = first_name + " " + last_name
print(full_name)



print("\n\n--------------------\n\n")

# To define an integer, use the following syntax:
mark_age = 20
print(mark_age)

print("\n\n--------------------\n\n")


# we can use the above trick to fomate the strings

# mark_name_and_age = full_name + " " + mark_age
# print(mark_name_and_age)

# hmmm we have a problem here?
# TypeError: cannot concatenate 'str' and 'int' objects

# so how to deal with it:
# string interpolation python
# 'Full name: {full_name} and his age is: {mark_age}'


print("Full name: {} and his age is: {} years old".format(full_name,mark_age))

# as we saw '\n' is a new line
# '\t' is Tap space

#                 Tier I          Tier II
# A's Bootcamp	3 6 months ago	14  1 year ago


print("\n\n--------------------\n\n")




















print("\t\tTier I\t\tTier II")
print("A's Bootcamp {}  {} months ago  {}  {} year ago".format(3,6,14,1))