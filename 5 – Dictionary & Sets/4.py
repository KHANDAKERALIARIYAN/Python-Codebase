# Python Set Methods from GPT

# 🔹 1. add(x) – Add an element
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

# 🔹 2. update(iterable) – Add multiple elements
s.update([5, 6])
print(s)  # Output: {1, 2, 3, 4, 5, 6}

# 🔹 3. remove(x) – Remove an element (KeyError if not found)
s.remove(2)
print(s)  # Output: {1, 3, 4, 5, 6}

# 🔹 4. discard(x) – Remove element if present (no error if not)
s.discard(10)  # Does nothing

# 🔹 5. pop() – Remove and return a random element
element = s.pop()
print(element)  # Output: (some element)

# 🔹 6. clear() – Remove all elements
s.clear()
print(s)  # Output: set()

# 🔹 7. copy() – Shallow copy
s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)  # Output: {1, 2, 3}

# 🔄 Set Operations
# 🔸 8. union(set2) or | – Combine elements
a = {1, 2}
b = {2, 3}
print(a.union(b))  # Output: {1, 2, 3}

# 🔸 9. intersection(set2) or & – Common elements
print(a.intersection(b))  # Output: {2}

# 🔸 10. difference(set2) or - – Items only in a
print(a.difference(b))  # Output: {1}

# 🔸 11. symmetric_difference(set2) or ^ – Items in either but not both
print(a.symmetric_difference(b))  # Output: {1, 3}

# 🔸 12. issubset(set2) – Check if all elements are in another set
print({1, 2}.issubset({1, 2, 3}))  # Output: True

# 🔸 13. issuperset(set2) – Check if it contains all elements of another set
print({1, 2, 3}.issuperset({1, 2}))  # Output: True

# 🔸 14. isdisjoint(set2) – Check if sets have no elements in common
print({1, 2}.isdisjoint({3, 4}))  # Output: True