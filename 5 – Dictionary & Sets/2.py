# Python Dictionary Methods from GPT

# 🔹 1. dict.keys() – Get all keys
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # Output: dict_keys(['name', 'age'])

# 🔹 2. dict.values() – Get all values
print(person.values())  # Output: dict_values(['Alice', 25])

# 🔹 3. dict.items() – Get all key-value pairs
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])

# 🔹 4. dict.get(key, default) – Safe value access
print(person.get('name'))        # Output: Alice
print(person.get('email', 'N/A'))  # Output: N/A (no error)

# 🔹 5. dict.update(other_dict) – Update dictionary with another
person.update({'age': 30, 'email': 'alice@example.com'})
print(person)  # Output: {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}

# 🔹 6. dict.pop(key, default) – Remove item by key
age = person.pop('age')
print(age)      # Output: 30
print(person)   # 'age' removed from dict

# 🔹 7. dict.popitem() – Remove and return last inserted pair
last = person.popitem()
print(last)  # Output: ('email', 'alice@example.com') (in Python 3.7+)

# 🔹 8. dict.clear() – Remove all items
person.clear()
print(person)  # Output: {}

# 🔹 9. dict.copy() – Shallow copy
original = {'a': 1, 'b': 2}
copy_dict = original.copy()
print(copy_dict)  # Output: {'a': 1, 'b': 2}

# 🔹 10. dict.setdefault(key, default) – Set default if key is missing
person = {'name': 'Bob'}
person.setdefault('age', 20)
print(person)  # Output: {'name': 'Bob', 'age': 20}

# 🔹 11. in operator – Check if key exists
print('name' in person)  # Output: True