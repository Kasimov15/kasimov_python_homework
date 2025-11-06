#lesson-2

#1 exercise
username = input("Enter your name:")
userbirthdate = input("Enter your birthdate:")
userage = 2025 - int(userbirthdate)
print(f"User's name is {username} and user's age is {userage}")


#2 exercise
cars = ["Lamborghini", "Mercedes", "Toyota", "Tesla", "BMW", "Audi"]
txt = 'LMaasleitbtui'
found = [car for car in cars if car.lower() in txt.lower()]
print("Found car names:", found) 


#3 exercise
cars = ["Lamborghini", "Mercedes", "Toyota", "Tesla", "BMW", "Audi"]
txt = 'MsaatmiazD'
found = [car for car in cars if car.lower() in txt.lower()]
print("Found car names:", found) 


#4 exercise
txt = "I'am John. I am from London"
residence_area = ["London", "New York", "Berlin", "Madrid"]
found = [area for area in residence_area if area.lower() in txt.lower()]
print("Found residence areas:", found)


#5 exercise
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)


#6 exercise
text = input("Enter a string:")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print("number of vowels:", vowel_count)


#7 exercise
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
maximum_value = max(numbers)
print("The maximum value is:", maximum_value)


#8 exercise
word = input("Enter a word: ")
word = word.lower()
if word == word[::-1]:
   print("It's a palindrome")
else:
   print("It's not a palindrome")


#9 exercise
email = input("Enter your email address: ")
parts = email.split('@')
if len(parts) == 2:
  domain = parts[1]
  print("The domain is:", domain)
else:
  print("Invalid email address")


#10 exercise
import random
import string
length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
