# chapter 4 practice set 

# 1.

fruits = []
f1=input("Enter first fruit: ")
fruits.append(f1)
f2=input("Enter second fruit: ")
fruits.append(f2)
f3=input("Enter third fruit: ")
fruits.append(f3)
f4=input("Enter fourth fruit: ")
fruits.append(f4)
f5=input("Enter fifth fruit: ")
fruits.append(f5)
f6=input("Enter sixth fruit: ")
fruits.append(f6)   
f7=input("Enter seventh fruit: ")
fruits.append(f7)
print(fruits)

# 2.

marks = []
m1=int(input("Enter first student marks: "))
marks.append(m1)
m2=int(input("Enter second student marks: "))
marks.append(m2)
m3=int(input("Enter third student marks: "))
marks.append(m3)
m4=int(input("Enter fourth student marks: "))
marks.append(m4)
m5=int(input("Enter fifth student marks: "))
marks.append(m5)
m6=int(input("Enter sixth student marks: "))
marks.append(m6)
print(marks.sort())
print(marks)

# 3.

t= (1, 2, 3, 4, 5, 6, 7, 8, 9)
t[1]= 10  # Tuples are immutable, this will raise an error

# 4.

l1=[1,2,3,4]
print(sum(l1))  # Output: 10

# 5.
a = (7, 0, 8, 0, 0, 9) 
print(a.count(0))  # Output: 3