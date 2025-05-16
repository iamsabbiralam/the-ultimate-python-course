s = {1, 5, 32, 54, 5, 5, 5, "Harry"}
s.add(100)  # add an element to the set
print(s, type(s))
# properties of python sets
# 1. sets are unordered => elements order does not matter
# 2. sets are unindexed => cannot access elements using index
# 3. there is no way to change items in sets
# 4. sets cannot contain duplicate values
# s.remove(100)  # remove an element from the set
s.discard(200)  # remove an element from the set, does not raise an error if the element is not found
print(s)

# operations on sets
s1 = {1, 2, 3, 4}
# len(s1) # returns the number of elements in the set
print(len(s1))
s1.remove(1)  # remove an element from the set and return the element removed
print(s1)
s1.pop()  # remove and return an arbitrary element from the set
print(s1)
s1.clear()  # remove all elements from the set
print(s1)