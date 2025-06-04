# chapter 6 practice set 

# 1.

a1=int(input("Enter 1st number: "))
a2=int(input("Enter 2nd number: "))
a3=int(input("Enter 3rd number: "))
a4=int(input("Enter 4th number: "))
if (a1>a2 and a1>a3 and a1>a4):
    print("1st number is greatest")
elif (a2>a1 and a2>a3 and a2>a4):
    print("2nd number is greatest")
elif (a3>a1 and a3>a2 and a3>a4):
    print("3rd number is greatest")
elif (a4>a1 and a4>a2 and a4>a3):
    print("4th number is greatest")
else:
    print("All numbers are equal or there is no greatest number")

# 2.

a1=int(input("Enter 1st subject number: "))
a2=int(input("Enter 2nd subject number: "))
a3=int(input("Enter 3rd subject number: "))
avg=(a1+a2+a3)/3
if(a1>=33 and a2>=33 and a3>=33):
    if(avg>=40):
        print("You are pass")
    else:
        print("You are fail")
else:
    print("You are fail due to less than 33% in one or more subjects")

# 3.

p1="Make a lot of money"
p2="Buy now"
p3="Subscribe this"
p4="Click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam comment")
else:
    print("This is not a spam comment")

# 4.

username = input("Enter your username: ")
if(len(username) < 10):
    print("Username contains less than 10 characters")
else:
    print("Username contains 10 or more characters")

# 5.

li=["ariyan","rohan","sahil","rahik","boby"]
name=input("Enter your name: ")
if(name in li):
    print("Welcome to the group")
else:
    print("You are not in the group")

# 6.

marks=int(input("Enter your marks: "))
if(marks >= 90 and marks <= 100):
    print("You got Ex grade")
elif(marks >= 80 and marks < 90):
    print("You got A grade")
elif(marks >= 70 and marks < 80):
    print("You got B grade")
elif(marks >= 60 and marks < 70):
    print("You got C grade")
elif(marks >= 50 and marks < 60):
    print("You got D grade")
elif(marks < 50):
    print("You got F grade")
else:
    print("Invalid marks")

# 7. 

post=input("Enter your post: ")
name="Harry"
if(name.lower() in post.lower()):
    print("This is post is talking about Harry")
else:
    print("This post is not talking about Harry")
