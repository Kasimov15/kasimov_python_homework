import pandas as pd
import numpy as np

# =========================
# Homework 1
# =========================

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Rename columns
df = df.rename(columns={
    'First Name': 'first_name',
    'Age': 'age'
})

# Print first 3 rows
print("First 3 rows:")
print(df.head(3))

# Mean age
print("\nMean age:")
print(df['age'].mean())

# Select Name and City columns
print("\nName and City columns:")
print(df[['first_name', 'City']])

# Add Salary column with random values
df['Salary'] = np.random.randint(3000, 8000, size=len(df))

# Summary statistics
print("\nSummary statistics:")
print(df.describe())


# =========================
# Homework 2
# =========================

sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

print("\nMax sales and expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].max())

print("\nMin sales and expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].min())

print("\nAverage sales and expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].mean())


# =========================
# Homework 3
# =========================

expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# Set Category as index
expenses = expenses.set_index('Category')

print("\nMax expense for each category:")
print(expenses.max(axis=1))

print("\nMin expense for each category:")
print(expenses.min(axis=1))

print("\nAverage expense for each category:")
print(expenses.mean(axis=1))
