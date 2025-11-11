# Python Dictionary and Set Exercises

# Dictionary Exercises
my_dict = {'a': 3, 'b': 1, 'c': 2}
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", ascending)
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", descending)

d = {0: 10, 1: 20}
d[2] = 30
print("Updated dictionary:", d)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {}
for dic in (dic1, dic2, dic3):
    result.update(dic)
print("Concatenated dictionary:", result)

n = 5
squares = {}
for x in range(1, n + 1):
    squares[x] = x * x
print("Dictionary with squares:", squares)

squares_15 = {x: x*x for x in range(1, 16)}
print("Squares from 1 to 15:", squares_15)

# Set Exercises
my_set = {"apple", "banana", "cherry"}
print("Created set:", my_set)

for item in my_set:
    print("Iterating:", item)

my_set.add("orange")
my_set.update(["mango", "grape"])
print("After adding members:", my_set)

my_set.remove("banana")
print("After removing item:", my_set)

if "apple" in my_set:
    my_set.remove("apple")
print("After conditional removal:", my_set)
