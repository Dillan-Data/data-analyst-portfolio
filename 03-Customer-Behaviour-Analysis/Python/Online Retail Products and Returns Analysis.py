import pandas as pd

df = pd.read_csv('online_retail_cleaned.csv', parse_dates=['invoice_date'])

# Total Sales Per Product
product_sales = (df[~df['is_return']].groupby(['stockcode', 'description'])['total_sales']
                 .sum()
                 .reset_index()
                 .sort_values('total_sales', ascending=False))

print(product_sales.head())

# Quantity Vs Revenue
product_quantity = (df[~df['is_return']]
                    .groupby(['stockcode', 'description'])['abs_quantity']
                    .sum()
                    .reset_index()
                    .sort_values('abs_quantity', ascending=False))

print(product_quantity.head(10))

# products most often returned
returns_count = (df[df['is_return']]
                 .groupby(['stockcode', 'description'])['abs_quantity']
                 .sum()
                 .reset_index()
                 .sort_values('abs_quantity', ascending=False))

print(returns_count.head(10))

# Return Rate per Product - Which products cause the most operational pain?
sales_units = (df[df['is_return']]
               .groupby('stockcode')['abs_quantity']
               .sum()
)

return_units = (df[df['is_return']]
                .groupby('stockcode')['abs_quantity']
                .sum()
                )

product_returns = (pd.concat([sales_units, return_units], axis=1)
                   .fillna(0)
                   .reset_index()
                   )

product_returns.columns = ['stockcode', 'sold_units', 'returned_units']

product_returns['return_rate'] = (
    product_returns['returned_units'] / (product_returns['sold_units'] + product_returns['returned_units'])
)

product_returns = product_returns.sort_values('return_rate', ascending=False)

print(product_returns.head(10))

# Revenue Lost to Returns
return_value = (df[df['is_return']]
                .groupby(['stockcode', 'description'])['total_sales']
                .sum()
                .reset_index()
                .sort_values('total_sales')
                )

print(return_value.head(10))

# Export for Power BI and Reporting
product_sales.to_csv("product_sales_summary.csv", index=False)
product_quantity.to_csv("product_quantity_summary.csv", index=False)
returns_count.to_csv("product_returns_summary.csv", index=False)
product_returns.to_csv("product_return_rates.csv", index=False)
return_value.to_csv("product_return_value.csv", index=False)
