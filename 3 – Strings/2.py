# string functions 
name=" Khandaker Ali Ariyan "
print(name)

# 1. lower(), upper(), capitalize(), title()
s = "hello world"
print(s.lower())      # "hello world"
print(s.upper())      # "HELLO WORLD"
print(s.capitalize()) # "Hello world"
print(s.title())      # "Hello World"

# 2. strip(), lstrip(), rstrip()
s = "   hello world   "
print(s.strip())   # "hello world"
print(s.lstrip())  # "hello world   "
print(s.rstrip())  # "   hello world"

# 3. replace(old, new)
s = "banana"
print(s.replace("a", "o"))  # "bonono"

# 4. split(), join()
# split()
s = "apple,banana,cherry"
fruits = s.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']
# join()
words = ['Python', 'is', 'fun']
sentence = " ".join(words)
print(sentence)  # "Python is fun"

# 5. find(), rfind()
s = "hello world"
print(s.find("o"))    # 4 (first occurrence)
print(s.rfind("o"))   # 7 (last occurrence)

# 6. startswith(), endswith()
s = "hello world"
print(s.startswith("hello"))  # True
print(s.endswith("world"))    # True

# 7. isdigit(), isalpha(), isalnum(), isspace()
print("123".isdigit())   # True
print("abc".isalpha())   # True
print("abc123".isalnum())# True
print("   ".isspace())   # True

# 8. count()
s = "banana"
print(s.count("a"))  # 3

# 9. format() / f-strings
name = "Alice"
age = 30
print("My name is {} and I am {} years old".format(name, age))
# or
print(f"My name is {name} and I am {age} years old")

# 10. casefold() (like lower(), but more aggressive – good for Unicode)
print("straße".casefold())  # "strasse"