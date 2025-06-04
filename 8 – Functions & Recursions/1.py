# Function 
def average():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    avg=(a+b+c)/3
    print("The average of the three numbers is: ", avg)

average()

def greeting():
    name=input("Enter your name: ")
    print(f"Hello {name} there! Good Morning!")

greeting()

# Quick Quiz:  Write a program to greet a user with “Good day” using functions. 
def greet():
    print("Good day!")
greet()

def greet(name):
    print(f"Good {name} day!")
greet()

def goodDay(name,ending="Thank you"):
    print(f"Good {name} day! {ending}")
goodDay("John")

