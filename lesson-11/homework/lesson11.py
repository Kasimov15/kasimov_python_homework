# ======================================
# VIRTUAL ENV NOTE (COMMENT ONLY)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# ======================================
# string_utils.py (MODULE)
# ======================================

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# ======================================
# geometry package → circle.py
# ======================================

import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius


# ======================================
# file_operations package
# ======================================

def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


# ======================================
# TESTING EVERYTHING (MAIN PROGRAM)
# ======================================

if __name__ == "__main__":

    print("=== Math Operations ===")
    print("Add:", add(5, 3))
    print("Subtract:", subtract(10, 4))
    print("Multiply:", multiply(2, 6))
    print("Divide:", divide(8, 2))

    print("\n=== String Utils ===")
    print("Reverse:", reverse_string("hello"))
    print("Vowels:", count_vowels("education"))

    print("\n=== Geometry ===")
    print("Circle Area:", calculate_area(5))
    print("Circle Circumference:", calculate_circumference(5))

    print("\n=== File Operations ===")
    write_file("test.txt", "Hello Python World")
    print("File Content:", read_file("test.txt"))
