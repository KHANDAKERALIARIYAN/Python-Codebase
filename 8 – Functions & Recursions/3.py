# chapter 8 practice set 

# 1.

def greatestNumber(a,b,c):
    if(a>b) and (a>c):
        return a
    elif(b>a) and (b>c):
        return b
    else:
        return c

print("The greatest number is: ", greatestNumber(10, 20, 30))

# 2.

def celciusToFarenheit(celcius):
    return (celcius*(9/5))+32

print("The temperature in Farenheit is: ", celciusToFarenheit(30))

# 3.

a=10
b=20
c=30
d=40
print(a)
print(b)
print(c,end="")
print(d,end="")

# 4.

def sumOfN(n):
    return n*(n+1)//2

print("The sum of first n natural numbers is: ", sumOfN(10))

# 5.

def printStar(n):
    if(n==0):
        return
    print("*" * n)
    printStar(n-1)

printStar(5)

# 6.

def inchesToCentimeters(inches):
    return inches * 2.54

print("The length in centimeters is: ", inchesToCentimeters(10))

# 7.

def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l=["apple", "banana", "cherry", "apple", "date"]

print(rem(l, "apple"))  # Output: ['banana', 'cherry', 'date']

# 8.

def multiplicationTable(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

multiplicationTable(5)