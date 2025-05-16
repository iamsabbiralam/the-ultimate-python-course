# can we have a set with 18(int) and '18'(str) as a value in it?
s = set()  # create an empty set
s.add(18)  # add the number to the set
s.add('18')  # add the string to the set
print(s)  # {18, '18'}
