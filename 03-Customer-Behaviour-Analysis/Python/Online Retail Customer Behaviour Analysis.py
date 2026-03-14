import pandas as pd

df = pd.read_csv("online_retail_cleaned.csv", parse_dates=["invoice_date"])

# remove returns from customer behaviour analysis
df = df[~df['is_return']]

# Customer_overview
customer_overview = {
    "total_customers": df['customerid'].nunique(),
    "total_orders": df['invoiceno'].nunique(),
    'avg_orders_per_customer': round(
        df['invoiceno'].nunique() / df['customerid'].nunique(), 2
    )
}

print("\n --- CUSTOMER OVERVIEW ---")
for k, v in customer_overview.items():
    print(f"{k}: {v}")

# customer spend
customer_spend = (
    df.groupby('customerid')['total_sales']
    .sum()
    .reset_index()
)

print(customer_spend.describe())


# top customers
top_customers = (
    customer_spend.sort_values('total_sales', ascending=False).head(10)
)

print(top_customers)

# Orders Per Customer
orders_per_customer = (
    df.groupby('customerid')['invoiceno'].nunique().reset_index(name='order_count')
)

repeat_customers = orders_per_customer[orders_per_customer['order_count']> 1]
one_time_customers = orders_per_customer[orders_per_customer['order_count'] == 1]
print(f'Repeat Customers: {len(repeat_customers)}')
print(f'One-Time Customers: {len(one_time_customers)}')

# Customer Geography
customer_country = (
    df.groupby("country")["customerid"]
    .nunique()
    .reset_index(name="customer_count")
    .sort_values("customer_count", ascending=False)
)

print(customer_country.head())

#EXPORT
customer_spend.to_csv('customer_spend_summary.csv', index=False)
orders_per_customer.to_csv('customer_order_frequency.csv', index=False)
customer_country.to_csv('customer_country_distribution.csv', index=False)