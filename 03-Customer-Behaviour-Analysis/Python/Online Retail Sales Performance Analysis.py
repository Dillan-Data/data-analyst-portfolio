# Import 
import pandas as pd

df = pd.read_csv("online_retail_cleaned.csv", parse_dates=["invoice_date"])

# --- SALES PERFORMANCE ---

# Separate sales and returns
sales = df[~df["is_return"]]
returns = df[df["is_return"]]

# KPI summary
sales_kpis = {
    "gross_sales": sales["total_sales"].sum(),
    "returns_value": returns["total_sales"].sum(),
    "net_sales": df["total_sales"].sum(),
    "total_orders": df["invoiceno"].nunique()
}

print("\n--- SALES KPIs ---")
for k, v in sales_kpis.items():
    print(f"{k}: {round(v, 2)}")

# Monthly sales
monthly_sales = (
    sales
    .groupby(["year", "month", "month_name"])["total_sales"]
    .sum()
    .reset_index()
    .sort_values(["year", "month"])
)

print(monthly_sales.head())
