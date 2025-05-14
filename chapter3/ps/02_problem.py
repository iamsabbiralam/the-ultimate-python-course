# write a program to fill in a letter template given below with name and date.
""" letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>''' """
# name = input("Enter your name: ")
# date = input("Enter the date: ")
# print(f"Dear {name},\nYou are selected!\n{date}")

letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''
print(letter.replace("<|NAME|>", "John").replace("<|DATE|>", "14th May2025"))