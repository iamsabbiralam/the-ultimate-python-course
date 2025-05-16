# write a program to input eight numbers from the user and display all the unique number (once)
s = set()  # create an empty set
n = input("Enter number 1: ")
s.add(int(n))  # add the number to the set
n = input("Enter number 2: ")
s.add(int(n))  # add the number to the set
n = input("Enter number 3: ")
s.add(int(n))  # add the number to the set
n = input("Enter number 4: ")
s.add(int(n))  # add the number to the set
n = input("Enter number 5: ")
s.add(int(n))  # add the number to the set
n = input("Enter number 6: ")
s.add(int(n))  # add the number to the set
n = input("Enter number 7: ")
s.add(int(n))  # add the number to the set
n = input("Enter number 8: ")
s.add(int(n))  # add the number to the set
print("The unique numbers are: ", s)  # print the set
