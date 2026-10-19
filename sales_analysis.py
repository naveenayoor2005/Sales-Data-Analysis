
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load sales data
df = pd.read_csv("sales.csv")

# Clean and prepare data
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["Price"]
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Key performance indicators
total_revenue = df["Revenue"].sum()
total_units = df["Quantity"].sum()
total_orders = df["OrderID"].nunique()
average_order_value = total_revenue / total_orders

# Product analysis
product_quantity = df.groupby("Product")["Quantity"].sum()
product_revenue = df.groupby("Product")["Revenue"].sum()

top_selling_product = product_quantity.idxmax()
top_revenue_product = product_revenue.idxmax()

# Monthly analysis
monthly_revenue = df.groupby("Month")["Revenue"].sum()
best_month = monthly_revenue.idxmax()

# Category analysis
category_revenue = df.groupby("Category")["Revenue"].sum()
top_category = category_revenue.idxmax()

# Display results
print("\n===== SALES ANALYSIS REPORT =====")
print(f"Total Revenue: Rs. {total_revenue:,.2f}")
print(f"Total Units Sold: {total_units}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: Rs. {average_order_value:,.2f}")

print("\nQuantity Sold by Product:")
print(product_quantity.sort_values(ascending=False))

print("\nRevenue by Product:")
print(product_revenue.sort_values(ascending=False))

print("\nMonthly Revenue:")
print(monthly_revenue)

print("\nRevenue by Category:")
print(category_revenue.sort_values(ascending=False))

print(f"\nTop-selling product by quantity: {top_selling_product}")
print(f"Product generating highest revenue: {top_revenue_product}")
print(f"Best month: {best_month}")
print(f"Top revenue category: {top_category}")

# Save product quantity chart
product_quantity.sort_values(ascending=False).plot(
    kind="bar", title="Quantity Sold by Product"
)
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.savefig("product_sales.png")
plt.close()

# Save monthly revenue chart
monthly_revenue.plot(
    kind="bar", title="Monthly Revenue"
)
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.close()

# Save category revenue chart
category_revenue.plot(
    kind="bar", title="Revenue by Category"
)
plt.xlabel("Category")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("category_revenue.png")
plt.close()

# Generate business insights report
report = f"""# Sales Data Analysis: Business Insights

## Dataset Summary
- Total revenue: Rs. {total_revenue:,.2f}
- Total units sold: {total_units}
- Unique orders: {total_orders}
- Average order value: Rs. {average_order_value:,.2f}

## Key Findings
- Top product by quantity sold: {top_selling_product}
  ({product_quantity[top_selling_product]} units).
- Highest-revenue product: {top_revenue_product}
  (Rs. {product_revenue[top_revenue_product]:,.2f}).
- Highest-revenue month: {best_month}
  (Rs. {monthly_revenue[best_month]:,.2f}).
- Highest-revenue category: {top_category}
  (Rs. {category_revenue[top_category]:,.2f}).

## Business Recommendations
1. Review laptop pricing, costs, and inventory because laptops
   generate the highest product revenue.
2. Maintain suitable mouse inventory because it has the highest
   sales quantity in this dataset.
3. Investigate what contributed to March's higher revenue and
   check whether the pattern continues in future months.
4. Compare product costs and profit margins before deciding
   which products are the most profitable.

## Limitations
This is a small sample dataset covering three months.
Revenue is not the same as profit because product costs,
operating expenses, and other costs are not provided.
The findings should not be treated as evidence of long-term trends.
"""

Path("insights.md").write_text(report, encoding="utf-8")

print("\nCharts saved successfully.")
print("Business insights saved to insights.md")
print("Analysis completed!")
