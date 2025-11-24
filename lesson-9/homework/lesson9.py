import math
from datetime import datetime

# ============================================================
# 1. Circle Class
# ============================================================

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# ============================================================
# 2. Person Class
# ============================================================

class Person:
    def __init__(self, name, country, birthdate):  # birthdate: "YYYY-MM-DD"
        self.name = name
        self.country = country
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    def age(self):
        today = datetime.today()
        return today.year - self.birthdate.year - (
            (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
        )


# ============================================================
# 3. Calculator Class
# ============================================================

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Error: division by zero"
        return a / b


# ============================================================
# 4. Shape + Subclasses
# ============================================================

class Shape:
    def area(self):
        raise NotImplementedError("area() must be overridden")

    def perimeter(self):
        raise NotImplementedError("perimeter() must be overridden")


class CircleShape(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def perimeter(self):
        return 2 * math.pi * self.r


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = self.b = self.c = None
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# ============================================================
# 5. Binary Search Tree Class
# ============================================================

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(root, key):
            if root is None:
                return Node(key)
            if key < root.key:
                root.left = _insert(root.left, key)
            else:
                root.right = _insert(root.right, key)
            return root

        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(root, key):
            if root is None:
                return False
            if root.key == key:
                return True
            if key < root.key:
                return _search(root.left, key)
            return _search(root.right, key)

        return _search(self.root, key)


# ============================================================
# 6. Stack Data Structure
# ============================================================

class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.data:
            return "Stack is empty!"
        return self.data.pop()


# ============================================================
# 7. Linked List Data Structure
# ============================================================

class NodeLL:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        cur = self.head
        while cur:
            print(cur.value, end=" -> ")
            cur = cur.next
        print("None")

    def insert(self, value):
        new = NodeLL(value)
        new.next = self.head
        self.head = new

    def delete(self, value):
        cur = self.head
        prev = None
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return
            prev = cur
            cur = cur.next


# ============================================================
# 8. Shopping Cart Class
# ============================================================

class ShoppingCart:
    def __init__(self):
        self.items = {}  # item: price

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_price(self):
        return sum(self.items.values())


# ============================================================
# 9. Stack with Display
# ============================================================

class DisplayStack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.data:
            return "Stack empty!"
        return self.data.pop()

    def display(self):
        print("Stack:", self.data)


# ============================================================
# 10. Queue Data Structure
# ============================================================

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if not self.q:
            return "Queue empty!"
        return self.q.pop(0)


# ============================================================
# 11. Bank Class
# ============================================================

class Bank:
    def __init__(self):
        self.accounts = {}  # name: balance

    def create_account(self, name, balance=0):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        self.accounts[name] += amount

    def withdraw(self, name, amount):
        if self.accounts[name] >= amount:
            self.accounts[name] -= amount
        else:
            return "Insufficient funds"

    def get_balance(self, name):
        return self.accounts[name]


# ============================================================
# END OF CODE
# ============================================================

print("All OOP classes loaded successfully!")
