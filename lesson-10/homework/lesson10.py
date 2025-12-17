# ==============================
# HOMEWORK PROJECTS 
# ==============================

from datetime import datetime

# ==============================
# HOMEWORK 1: TODO LIST APP
# ==============================

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓ Completed" if self.completed else "✗ Incomplete"
        return f"{self.title} | {self.description} | Due: {self.due_date} | {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("Invalid task number.")

    def list_all_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if not task.completed:
                print(task)


# ==============================
# HOMEWORK 2: BLOG SYSTEM
# ==============================

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date = datetime.now()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.date.strftime('%Y-%m-%d %H:%M')})"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for i, post in enumerate(self.posts):
            print(f"{i}. {post}")

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author.lower() == author.lower():
                print(post)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]
        else:
            print("Invalid post number.")

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content = new_content
        else:
            print("Invalid post number.")

    def latest_posts(self, count=3):
        for post in self.posts[-count:]:
            print(post)


# ==============================
# HOMEWORK 3: BANKING SYSTEM
# ==============================

class Account:
    def __init__(self, number, name, balance=0):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Overdraft not allowed.")
            return False
        self.balance -= amount
        return True

    def __str__(self):
        return f"Account {self.number} | {self.name} | Balance: ${self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.number] = account

    def get_account(self, number):
        return self.accounts.get(number)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)

        if sender and receiver and sender.withdraw(amount):
            receiver.deposit(amount)
            print("Transfer successful.")
        else:
            print("Transfer failed.")


# ==============================
# MAIN MENU (CLI)
# ==============================

def main():
    todo = ToDoList()
    blog = Blog()
    bank = Bank()

    while True:
        print("\n=== MAIN MENU ===")
        print("1. ToDo List")
        print("2. Blog System")
        print("3. Banking System")
        print("0. Exit")

        choice = input("Choose: ")

        # TODO MENU
        if choice == "1":
            print("\n--- ToDo Menu ---")
            print("1. Add Task")
            print("2. Complete Task")
            print("3. List All Tasks")
            print("4. List Incomplete Tasks")

            c = input("Choose: ")

            if c == "1":
                t = input("Title: ")
                d = input("Description: ")
                due = input("Due Date: ")
                todo.add_task(Task(t, d, due))

            elif c == "2":
                todo.list_all_tasks()
                i = int(input("Task number: "))
                todo.mark_task_complete(i)

            elif c == "3":
                todo.list_all_tasks()

            elif c == "4":
                todo.list_incomplete_tasks()

        # BLOG MENU
        elif choice == "2":
            print("\n--- Blog Menu ---")
            print("1. Add Post")
            print("2. List Posts")
            print("3. Posts by Author")
            print("4. Delete Post")
            print("5. Edit Post")
            print("6. Latest Posts")

            c = input("Choose: ")

            if c == "1":
                title = input("Title: ")
                content = input("Content: ")
                author = input("Author: ")
                blog.add_post(Post(title, content, author))

            elif c == "2":
                blog.list_posts()

            elif c == "3":
                author = input("Author name: ")
                blog.posts_by_author(author)

            elif c == "4":
                blog.list_posts()
                i = int(input("Post number: "))
                blog.delete_post(i)

            elif c == "5":
                blog.list_posts()
                i = int(input("Post number: "))
                new_title = input("New title: ")
                new_content = input("New content: ")
                blog.edit_post(i, new_title, new_content)

            elif c == "6":
                blog.latest_posts()

        # BANK MENU
        elif choice == "3":
            print("\n--- Bank Menu ---")
            print("1. Add Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Account Details")

            c = input("Choose: ")

            if c == "1":
                num = input("Account number: ")
                name = input("Holder name: ")
                bal = float(input("Initial balance: "))
                bank.add_account(Account(num, name, bal))

            elif c == "2":
                num = input("Account number: ")
                amt = float(input("Amount: "))
                bank.get_account(num).deposit(amt)

            elif c == "3":
                num = input("Account number: ")
                amt = float(input("Amount: "))
                bank.get_account(num).withdraw(amt)

            elif c == "4":
                f = input("From account: ")
                t = input("To account: ")
                amt = float(input("Amount: "))
                bank.transfer(f, t, amt)

            elif c == "5":
                num = input("Account number: ")
                print(bank.get_account(num))

        elif choice == "0":
            print("Goodbye!")
            break


# ==============================
# RUN PROGRAM
# ==============================

if __name__ == "__main__":
    main()
