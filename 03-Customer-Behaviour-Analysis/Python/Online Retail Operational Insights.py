import pandas as pd

df = pd.read_csv('online_retail_cleaned.csv', parse_dates=['invoice_date'])

# Sales by Weekday - When should staff, logistics, and promotions be focused?
weekday_sales = (df[~df['is_return']]
                 .groupby('weekday')['total_sales']
                 .sum()
                 .reset_index()
                 .sort_values('total_sales', ascending=False))

print(weekday_sales)

# Sales by Hour - Peak Hours - Operational Inefficiencies
hourly_sales = (df[~df['is_return']]
                .groupby('hour')['total_sales']
                .sum()
                .reset_index()
                )

print(hourly_sales.head())

# Returns by Weekday 
weekday_returns = (df[df['is_return']]
                   .groupby('weekday')['abs_quantity']
                   .sum()
                   .reset_index()
                   .sort_values('abs_quantity', ascending=False)
                   )

print(weekday_returns)

# Order Size Analysis - typical order size - Bulk orders?
order_sizes = (
    df.groupby('invoiceno')['abs_quantity']
    .sum()
    .reset_index(name='items_per_order')
)

print(order_sizes.describe())

# Country Operations
country_orders = (
    df.groupby('country')['invoiceno']
    .nunique()
    .reset_index(name='order_count')
    .sort_values('order_count', ascending=False)
)

print(country_orders.head())


weekday_sales.to_csv("ops_sales_by_weekday.csv", index=False)
hourly_sales.to_csv("ops_sales_by_hour.csv", index=False)
weekday_returns.to_csv("ops_returns_by_weekday.csv", index=False)
order_sizes.to_csv("ops_order_size_distribution.csv", index=False)
country_orders.to_csv("ops_country_orders.csv", index=False)
