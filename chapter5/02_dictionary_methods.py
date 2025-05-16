marks = {
      "Alice": 85,
      "Bob": 90,
      "Charlie": 78,
      0: "Alice"
}
# print(marks.items()) # Returns a view object that displays a list of a dictionary's key-value tuple pairs
# print(marks.keys()) # Returns a view object that displays a list of all the keys in the dictionary
print(marks.values()) # Returns a view object that displays a list of all the values in the dictionary
# marks.update({"Alice": 90, "Sabbir": 45}) # Updates the dictionary with the specified key-value pairs
# print(marks)
print(marks.get("Alice2")) # Returns the value of the specified key
print(marks["Alice2"]) # Returns the value of the specified key
