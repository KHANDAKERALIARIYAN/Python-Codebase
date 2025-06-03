# chapter 5 practice set  

# 1.
dictionary = {
    "Kemon" : "Hello",
    "Bhalo" : "Good",
    "Amar" : "My",
    "Naam" : "Name",
    "Tumi" : "You",
    "Ki" : "What"
}

word= input("Enter a word in Bangla: ")
print(dictionary[word])

# 2.
s=set()
n=int(input("Enter the number : "))
s.add(n)
n=int(input("Enter the number : "))
s.add(n)
n=int(input("Enter the number : "))
s.add(n)
n=int(input("Enter the number : "))
s.add(n)
n=int(input("Enter the number : "))
s.add(n)
n=int(input("Enter the number : "))
s.add(n)
n=int(input("Enter the number : "))
s.add(n)
n=int(input("Enter the number : "))
s.add(n)
print("The set is: ", s)

# 3.
s=set()
s.add(18)
s.add("18")
print(s)

# 4.
s= set() 
s.add(20) 
s.add(20.0) 
s.add('20') 
print(len(s))  # Output: 2, because 20 and 20.0 are considered the same number in Python, and '20' is a string.

# 5.
s={}
print(type(s))  # Output: <class 'dict'>, because {} creates an empty dictionary in Python, not a set.

# 6.
d={}
name = input("Enter your friends name: ")
language = input("Enter your friends favourite language: ")
d.update({name: language})

name = input("Enter your friends name: ")
language = input("Enter your friends favourite language: ")
d.update({name: language})

name = input("Enter your friends name: ")
language = input("Enter your friends favourite language: ")
d.update({name: language})

name = input("Enter your friends name: ")
language = input("Enter your friends favourite language: ")
d.update({name: language})

print("The dictionary is: ", d)  

# 7.
# if names are same, then it will update the value of the key in the dictionary.

# 8.
# if the language is same, then it will not cause any problem, it will just update the value of the key in the dictionary.

# 9.
s = {8, 7, 12, "Harry", [1,2]}
# we can not add a list to a set because sets are unordered collections of unique elements, and lists are mutable.