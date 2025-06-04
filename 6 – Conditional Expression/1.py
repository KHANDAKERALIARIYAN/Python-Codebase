# Conditional Expression Example if elif else ladder

age=int(input("Enter your age: "))

if(age>18):
    print("You are an adult")
    print("You can vote")

elif(age==18):
    print("You are exactly 18 years old")
    print("You can vote for the first time")

elif(age<0):
    print("Invalid age entered")
    print("Please enter a valid age")

else:
    print("You are a minor")
    print("You cannot vote")