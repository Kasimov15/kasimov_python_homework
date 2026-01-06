import pandas as pd
import numpy as np
import sqlite3

# ============================================================================
# HOMEWORK ASSIGNMENT 1: Analyzing Sales Data
# ============================================================================

print("=" * 60)
print("Homework Assignment 1: Analyzing Sales Data")
print("=" * 60)

# Load data
df_sales = pd.read_csv('task/sales_data.csv')

# Task 1: Group by Category statistics
category_stats = df_sales.groupby('Category').agg(
    Total_Quantity_Sold=('Quantity', 'sum'),
    Average_Price=('Price', 'mean'),
    Max_Quantity=('Quantity', 'max')
).round(2).reset_index()

print("\nTask 1 - Category Statistics:")
print(category_stats.to_string(index=False))

# Task 2: Top-selling product in each category
product_sales = df_sales.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = product_sales.loc[product_sales.groupby('Category')['Quantity'].idxmax()]

print("\nTask 2 - Top-Selling Products:")
print(top_products.to_string(index=False))

# Task 3: Date with highest total sales
df_sales['Total_Sales'] = df_sales['Quantity'] * df_sales['Price']
daily_sales = df_sales.groupby('Date')['Total_Sales'].sum().reset_index()
max_sales_date = daily_sales.loc[daily_sales['Total_Sales'].idxmax()]

print("\nTask 3 - Date with Highest Sales:")
print(f"Date: {max_sales_date['Date']}")
print(f"Total Sales: ${max_sales_date['Total_Sales']:,.2f}")

# ============================================================================
# HOMEWORK ASSIGNMENT 2: Examining Customer Orders
# ============================================================================

print("\n" + "=" * 60)
print("Homework Assignment 2: Examining Customer Orders")
print("=" * 60)

# Load data
df_orders = pd.read_csv('task/customer_orders.csv')

# Task 1: Customers with 20+ orders
customer_order_counts = df_orders.groupby('CustomerID')['OrderID'].nunique()
customers_20plus = customer_order_counts[customer_order_counts >= 20].index.tolist()

print("\nTask 1 - Customers with 20+ orders:")
print(f"Count: {len(customers_20plus)}")
print(f"Customer IDs: {customers_20plus[:10]}{'...' if len(customers_20plus) > 10 else ''}")

# Task 2: Customers with average price > $120
customer_avg_price = df_orders.groupby('CustomerID')['Price'].mean()
customers_high_price = customer_avg_price[customer_avg_price > 120].index.tolist()

print("\nTask 2 - Customers with average price > $120:")
print(f"Count: {len(customers_high_price)}")
print(f"Customer IDs: {customers_high_price[:10]}{'...' if len(customers_high_price) > 10 else ''}")

# Task 3: Product totals with quantity >= 5
product_totals = df_orders.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Price', lambda x: (x * df_orders.loc[x.index, 'Quantity']).sum())
).reset_index()
products_filtered = product_totals[product_totals['Total_Quantity'] >= 5]

print("\nTask 3 - Products with total quantity >= 5:")
print(products_filtered.to_string(index=False))

# ============================================================================
# HOMEWORK ASSIGNMENT 3: Population Salary Analysis
# ============================================================================

print("\n" + "=" * 60)
print("Homework Assignment 3: Population Salary Analysis")
print("=" * 60)

# Connect to SQLite database and read data
conn = sqlite3.connect('task/population.db')
df_population = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# Read salary bands from Excel
df_salary_bands = pd.read_excel('task/population salary analysis.xlsx')

# Create salary categories function
def assign_salary_category(salary, bands_df):
    for _, row in bands_df.iterrows():
        if row['Min'] <= salary <= row['Max']:
            return row['Category']
    return 'Other'

# Assign categories
df_population['Salary_Category'] = df_population['Salary'].apply(
    lambda x: assign_salary_category(x, df_salary_bands)
)

# National level calculations
national_stats = df_population.groupby('Salary_Category').agg(
    Population_Count=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).round(2)
national_stats['Population_Percentage'] = (national_stats['Population_Count'] / len(df_population) * 100).round(2)

print("\nNational Level Statistics:")
print(national_stats.reset_index().to_string(index=False))

# State level calculations
state_stats = df_population.groupby(['State', 'Salary_Category']).agg(
    Population_Count=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).round(2)

# Calculate percentages for each state
state_totals = df_population.groupby('State')['Salary'].count()
state_stats = state_stats.reset_index()
state_stats['Population_Percentage'] = state_stats.apply(
    lambda row: (row['Population_Count'] / state_totals[row['State']] * 100).round(2), 
    axis=1
)

print("\n\nState Level Statistics (first 20 rows):")
print(state_stats.head(20).to_string(index=False))

# Save results to files
category_stats.to_csv('task1_category_statistics.csv', index=False)
top_products.to_csv('task1_top_products.csv', index=False)
products_filtered.to_csv('task2_products_filtered.csv', index=False)
national_stats.to_csv('task3_national_stats.csv')
state_stats.to_csv('task3_state_stats.csv', index=False)

print("\n" + "=" * 60)
print("✅ All assignments completed!")
print("Results saved to CSV files.")
print("=" * 60)
