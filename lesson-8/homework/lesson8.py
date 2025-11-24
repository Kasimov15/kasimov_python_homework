# =====================================================================
#                PYTHON EXCEPTION HANDLING HOMEWORK
# =====================================================================

print("\n================= EXCEPTION HANDLING TASKS =================\n")


# 1. ZeroDivisionError
def zero_division_task():
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        print(a / b)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")


# 2. Raise ValueError if input is not integer
def raise_value_error_task():
    try:
        x = input("Enter an integer: ")
        if not x.lstrip("-").isdigit():
            raise ValueError("Not a valid integer!")
        print("Valid integer:", x)
    except ValueError as e:
        print("Error:", e)


# 3. FileNotFoundError
def file_not_found_task():
    try:
        filename = input("Enter filename: ")
        f = open(filename, "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("Error: File does not exist!")


# 4. Raise TypeError for non-numerical input
def raise_type_error_task():
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        if not (a.replace(".", "", 1).isdigit() and b.replace(".", "", 1).isdigit()):
            raise TypeError("Inputs must be numbers!")
        print(float(a) + float(b))
    except TypeError as e:
        print("Error:", e)


# 5. PermissionError
def permission_error_task():
    try:
        f = open("/root/protected.txt", "r")
        print(f.read())
    except PermissionError:
        print("Error: You do not have permission to access this file.")


# 6. IndexError
def index_error_task():
    try:
        lst = [1, 2, 3]
        idx = int(input("Enter index: "))
        print(lst[idx])
    except IndexError:
        print("Error: Index out of range!")


# 7. KeyboardInterrupt
def keyboard_interrupt_task():
    try:
        x = input("Enter a number (Ctrl+C to cancel): ")
        print("You entered:", x)
    except KeyboardInterrupt:
        print("\nInput cancelled by user!")


# 8. ArithmeticError
def arithmetic_error_task():
    try:
        x = 10 / 0   # will cause ZeroDivisionError (ArithmeticError family)
    except ArithmeticError:
        print("Arithmetic error occurred!")


# 9. UnicodeDecodeError
def unicode_decode_task():
    try:
        with open("test.bin", "rb") as f:
            print(f.read().decode("utf-8"))
    except UnicodeDecodeError:
        print("Error: Invalid UTF-8 encoding!")


# 10. AttributeError
def attribute_error_task():
    try:
        lst = [1, 2, 3]
        lst.push(10)   # push() does not exist
    except AttributeError:
        print("Error: Attribute does not exist!")



# =====================================================================
#                     FILE INPUT / OUTPUT HOMEWORK
# =====================================================================

print("\n================= FILE I/O TASKS =================\n")


# 1. Read entire file
def read_entire_file(filename):
    with open(filename, "r") as f:
        return f.read()


# 2. Read first n lines
def read_first_n(filename, n):
    with open(filename, "r") as f:
        return "".join([f.readline() for _ in range(n)])


# 3. Append text and display
def append_text(filename, text):
    with open(filename, "a") as f:
        f.write(text + "\n")
    with open(filename, "r") as f:
        return f.read()


# 4. Read last n lines
def read_last_n(filename, n):
    with open(filename, "r") as f:
        return "".join(f.readlines()[-n:])


# 5. File to list
def file_to_list(filename):
    with open(filename, "r") as f:
        return f.readlines()


# 6. Read file to variable
def file_to_variable(filename):
    with open(filename, "r") as f:
        return f.read()


# 7. File to array (char array)
def file_to_array(filename):
    with open(filename, "r") as f:
        return list(f.read())


# 8. Longest words
def longest_words(filename):
    with open(filename, "r") as f:
        words = f.read().split()
    mx = max(len(w) for w in words)
    return [w for w in words if len(w) == mx]


# 9. Count lines
def count_lines(filename):
    with open(filename, "r") as f:
        return len(f.readlines())


# 10. Count word frequency
def word_frequency(filename):
    with open(filename, "r") as f:
        from collections import Counter
        return Counter(f.read().lower().split())


# 11. File size
import os
def file_size(filename):
    return os.path.getsize(filename)


# 12. Write list to file
def write_list(filename, lst):
    with open(filename, "w") as f:
        for x in lst:
            f.write(str(x) + "\n")


# 13. Copy file
def copy_file(src, dest):
    with open(src, "r") as f1:
        with open(dest, "w") as f2:
            f2.write(f1.read())


# 14. Combine lines from two files
def combine_files(f1, f2, out):
    with open(f1, "r") as a, open(f2, "r") as b, open(out, "w") as o:
        for x, y in zip(a, b):
            o.write(x.strip() + " " + y.strip() + "\n")


# 15. Read random line
import random
def random_line(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return random.choice(lines)


# 16. Check if file is closed
def is_closed(filename):
    f = open(filename, "r")
    f.close()
    return f.closed


# 17. Remove newline characters
def remove_newlines(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]


# 18. Count words in file
def count_words(filename):
    with open(filename, "r") as f:
        return len(f.read().replace(",", " ").split())


# 19. Extract characters into list
def extract_chars(filename):
    with open(filename, "r") as f:
        return list(f.read())


# 20. Generate 26 text files A.txt … Z.txt
def generate_alphabet_files():
    import string
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as f:
            f.write(letter + "\n")


print("\n=== All tasks loaded successfully! ===")
print("You can now call any function in this file.\n")
