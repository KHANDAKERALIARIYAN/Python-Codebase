# sets
s={1, 2, 3, 4, 5 ,1, 2, 3} # this is a set with duplicates removed
e=set() # this is an empty set

print(s) # Output: {1, 2, 3, 4, 5}
print(type(s)) # Output: <class 'set'>
s.add(6)  # Add an element
print(s)  # Output: {1, 2, 3, 4, 5, 6}
print(len(s))  # Output: 6 (length of the set)
s.remove(2)  # Remove an element (KeyError if not found)
print(s)  # Output: {1, 3, 4, 5, 6}

s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.union(s2))  # Combine elements: {1, 2, 3, 4, 5, 6}
print(s1.intersection(s2))  # Common elements: set() (no common elements)