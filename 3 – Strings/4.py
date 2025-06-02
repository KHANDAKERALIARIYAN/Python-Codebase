# chapter 3 practice set 

# 1.
name = input("Enter your name: ")
print("Good Afternoon " + name)
print(f"Good Afternoon {name}")

# 2.
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter.replace("<|Name|>", "Ariyan").replace("<|Date|>", "1st January 2024"))

# 3.
name = "Khandaker  Ali  Ariyan"
print(name.find("  "))

# 4.
name = "Khandaker  Ali  Ariyan"
print(name.replace("  "," "))

# 5.
letter = "Dear Harry, \n\tthis python course is nice.\n Thanks!" 
print(letter)