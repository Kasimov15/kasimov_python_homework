# lesson-3
# 1. Create and Access List Elements
fruits = ["apple", "banana", "cherry", "orange", "grape"]
print("Third fruit:", fruits[2])

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Concatenated list:", combined_list)

# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50, 60]
middle_index = len(numbers) // 2
new_list = [numbers[0], numbers[middle_index], numbers[-1]]
print("Extracted elements:", new_list)

# 4. Convert List to Tuple
movies = ["Inception", "Interstellar", "Matrix", "Avatar", "Titanic"]
movies_tuple = tuple(movies)
print("Movies tuple:", movies_tuple)

# 5. Check Element in a List
cities = ["London", "Paris", "Rome", "Tokyo"]
print("Is Paris in the list?", "Paris" in cities)

# 6. Duplicate a List Without Using Loops
nums = [1, 2, 3]
duplicated = nums * 2
print("Duplicated list:", duplicated)

# 7. Swap First and Last Elements of a List
swap_list = [10, 20, 30, 40, 50]
swap_list[0], swap_list[-1] = swap_list[-1], swap_list[0]
print("Swapped list:", swap_list)

# 8. Slice a Tuple
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Tuple slice (3 to 7):", numbers_tuple[3:8])

# 9. Count Occurrences in a List
colors = ["blue", "red", "blue", "green", "blue", "yellow"]
print("Count of 'blue':", colors.count("blue"))

# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger", "elephant")
print("Index of 'lion':", animals.index("lion"))

# 11. Merge Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged tuple:", merged_tuple)

# 12. Find the Length of a List and Tuple
sample_list = [1, 2, 3, 4]
sample_tuple = (5, 6, 7, 8)
print("Length of list:", len(sample_list))
print("Length of tuple:", len(sample_tuple))

# 13. Convert Tuple to List
tuple_nums = (10, 20, 30, 40, 50)
converted_list = list(tuple_nums)
print("Converted list:", converted_list)

# 14. Find Maximum and Minimum in a Tuple
num_tuple = (5, 9, 2, 7, 1, 10)
print("Maximum:", max(num_tuple))
print("Minimum:", min(num_tuple))

# 15. Reverse a Tuple
words = ("Python", "is", "fun")
reversed_tuple = words[::-1]
print("Reversed tuple:", reversed_tuple)



