# chapter 7 practice set 

# 1.

n=int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 2.

l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
    
# 3.

n=int(input("Enter a number: "))
i=1
while(i < 11):
    print(f"{n} x {i} = {n * i}")
    i += 1

# 4.

n = int(input("Enter a number: "))

for i in range(2,n):
    if(n%i==0):
        print("Number is not prime")
        break
else:
    print("Number is prime")

# 5.

n=int(input("Enter a number: "))
i=0
sum=0
while(i <= n):
    sum += i
    i += 1
print(sum)

# 6.

n=int(input("Enter a number: "))
i=1
factorial=1
while(i <= n):
    factorial *= i
    i += 1
print(f"The factorial of {n} is {factorial}")

# 7.

n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1) , end="")
    print("")

# 8.

n=int(input("Enter a number: "))
for i in range(1,n+1):
    print("*"*(i) , end="")
    print("")

# 9.

n=int(input("Enter a number: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*(n) , end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")

    print("")

# 10.

n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n}X{11-i}={n*(11-i)}")
