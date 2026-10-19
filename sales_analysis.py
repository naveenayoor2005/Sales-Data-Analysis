import pandas as pd
import matplotlib.pyplot as plt

# Load the sales dataset
df = pd.read_csv("sales.csv")

# Calculate revenue for each order
df["Revenue"] = df["Quantity"] * df["Price"]

# Display the dataset
print("\nSALES DATA")
print(df)

# Calculate total revenue
total_revenue = df["Revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# Find the best-selling products by quantity
product_sales = df.groupby("Product")["Quantity"].sum()
print("\nQuantity Sold by Product")
print(product_sales)

# Calculate monthly revenue
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Revenue"].sum()
print("\nMonthly Revenue")
print(monthly_sales)

# Create a product sales chart
product_sales.plot(kind="bar", title="Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()

# Create a monthly revenue chart
monthly_sales.plot(kind="bar", title="Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()

print("\nAnalysis completed successfully!")
