# create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. Print the dictionary.
d = {}  # empty dictionary
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update({name: language})
print(d)
# if the name of 2 friends are same; what will happen to the program in problem 6?
# solution: the value of the key will be updated. The last value will be stored in the dictionary.
