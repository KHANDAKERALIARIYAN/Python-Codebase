# quiz -  Write a program to print yes when the age entered by the user is greater than or equal to 18. 

age=int(input("Enter your age: "))
if(age>=18):
    print("Yes")
else:
    print("No")

# multiple if statements

age=int(input("Enter your age: "))

if(age%2==0):
    print("Age is even")

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