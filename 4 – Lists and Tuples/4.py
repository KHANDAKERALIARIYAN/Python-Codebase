# tuple functions from GPT

# 🔹 1. len() – Get the number of elements
t = (1, 2, 3, 4)
print(len(t))  # Output: 4

# 🔹 2. sum() – Get the sum of all elements (numeric tuples)
t = (10, 20, 30)
print(sum(t))  # Output: 60

# 🔹 3. max() – Get the maximum value
t = (5, 10, 3)
print(max(t))  # Output: 10

# 🔹 4. min() – Get the minimum value
t = (5, 10, 3)
print(min(t))  # Output: 3

# 🔹 5. tuple() – Convert from list or other iterable
lst = [1, 2, 3]
t = tuple(lst)
print(t)  # Output: (1, 2, 3)

# 🔹 6. .count(x) – Count how many times a value appears
t = (1, 2, 2, 3, 2)
print(t.count(2))  # Output: 3

# 🔹 7. .index(x) – Find the first index of a value
t = (4, 5, 6, 5)
print(t.index(5))  # Output: 1

# 🔹 8. Tuple Unpacking – Assign values directly
person = ('John', 30, 'Teacher')
name, age, job = person
print(name)  # John
print(age)   # 30
print(job)   # Teacher

# 🔁 9. Iterating Over a Tuple
colors = ('red', 'green', 'blue')
for color in colors:
    print(color)

# 🧮 10. Membership Check: in and not in
t = (1, 2, 3)
print(2 in t)      # Output: True
print(5 not in t)  # Output: True

# 🧩 11. Nested Tuples
nested = (1, (2, 3), (4, 5))
print(nested[1])       # Output: (2, 3)
print(nested[1][1])   # Output: 3

# 🔄 12. Tuple Concatenation
a = (1, 2)
b = (3, 4)
c = a + b
print(c)  # Output: (1, 2, 3, 4)

# 🔁 13. Tuple Repetition
t = (0,) * 5
print(t)  # Output: (0, 0, 0, 0, 0)

# ⚙️ 14. Using Tuples as Dictionary Keys (because they are immutable)
locations = {
    (23.5, 45.3): "Dhaka",
    (40.7, -74.0): "New York"
}
print(locations[(40.7, -74.0)])  # Output: New York

# 📦 15. Tuple Packing and Unpacking
# Packing
info = "Alice", 24, "Engineer"
print(info)  # Output: ('Alice', 24,'Engineer')
# Unpacking
name, age, profession = info
print(profession)  # Output: Engineer

# 🔄 16. Swap Variables using Tuple
a = 5
b = 10
a, b = b, a
print(a, b)  # Output: 10 5

# 🧠 17. Slicing a Tuple
t = (0, 1, 2, 3, 4, 5)
print(t[1:4])     # Output: (1, 2, 3)
print(t[:3])      # Output: (0, 1, 2)
print(t[-2:])     # Output: (4, 5)

# 🔒 18. Immutable Nature Example
t = (1, 2, 3)
# t[0] = 5  # ❌ TypeError: 'tuple' object does not support item assignment