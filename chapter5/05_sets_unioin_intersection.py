s1 = {1, 45, 6, 5}
s2 = {7, 8, 1, 78, 5}
print(s1.union(s2))  # returns a new set with all elements from both sets
print(s1.intersection(s2))  # returns a new set with elements common to both sets
print(s1.issubset(s1))  # returns True if s1 is a subset of s2
print(s2.issuperset(s2))  # returns True if s1 is a superset of s2
