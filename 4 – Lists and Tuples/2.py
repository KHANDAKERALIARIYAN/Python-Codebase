# some function in list from GPT 

# 1. len() Length of a list
fruits = ['apple', 'banana', 'cherry']
print(len(fruits))  # Output: 3

# 2. append() Add item to the end
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# 3. extend() Add multiple items
fruits.extend(['grape', 'kiwi'])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'grape', 'kiwi']]

# 4. insert() Insert at a specific position
fruits.insert(1, 'mango')
print(fruits)  # Output: ['apple', 'mango', 'banana', ...]

# 5. remove() Remove by value
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'mango', 'cherry', ...]

# 6. pop() Remove by index (last by default)
last_item = fruits.pop()
print(last_item)  # Output: 'kiwi'
print(fruits)     # List without last item

# 7. index() Find index of item
i = fruits.index('apple')
print(i)  # Output: 0

# 8. count() Count occurrences
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.count(2))  # Output: 3

# 9. sort() Sort list in place
numbers.sort()
print(numbers)  # Output: [1, 2, 2, 2, 3, 4]

# 10. reverse() Reverse list in place
numbers.reverse()
print(numbers)  # Output: [4, 3, 2, 2, 2, 1]

# 11. copy() Create a copy
new_list = numbers.copy()
print(new_list)  # Same as numbers

# 12. clear() Empty the list
fruits.clear()
print(fruits)  # Output: []

# 13. sum(), max(), min()
nums = [10, 20, 30]
print(sum(nums))  # Output: 60
print(max(nums))  # Output: 30
print(min(nums))  # Output: 10

# 14. sorted() Return a new sorted list (original is unchanged)
unsorted = [5, 2, 9, 1]
sorted_list = sorted(unsorted)
print(sorted_list)  # Output: [1, 2, 5, 9]
print(unsorted)     # Original remains unchanged