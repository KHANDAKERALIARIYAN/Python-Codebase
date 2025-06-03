# List is mutable
random=["apple", "banana", "cherry",6, 8, 9, 10, "orange", "kiwi", "melon", "mango"]
print(random[0])
print(random.append("grape")) # append adds an element to the end of the list
print(random)

l1=[1,4,5,90,87,900,100,200,300,400,500]
print(l1)
print(l1.sort()) # sort sorts the list in ascending order
print(l1)
print(l1.reverse()) # reverse reverses the order of the list
print(l1)
print(l1.insert(0, 1000)) # insert adds an element at a specific index
poping = l1.pop(0) # pop removes the last element by default, or the element at the specified index
print(poping) # pop removes the element at the specified index and returns it
print(l1.remove(100)) # remove removes the first occurrence of the specified element