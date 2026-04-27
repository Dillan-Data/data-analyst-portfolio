import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('g:\Data Analysis Portfolio\Synthetics Sales\DATA\Synthetic_Sales_data.csv')

# 1 inspect data
#print(df.head(10))

# create visual functions for sales data
# 1 Set global presentation style (ALWAYS DO THIS FIRST)
def set_presentation_style():
    plt.style.use('default')
    plt.rcParams.update({
        'figure.figsize': (8,6),
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'axes.edgecolor': '#1f3c88',
        'axes.facecolor': 'white',
        'axes.grid': True,
        'grid.color': '#e0e0e0',
        'grid.linestyle': '--',
        'grid.alpha': 0.7,
        'xtick.color': '#1f3c88',
        'ytick.color': '#1f3c88',
        'font.family': 'DejaVu Sans'
    })

set_presentation_style()


# 1 Revenue Trend Over Time
def plot_revenue_trend(df):
    monthly_revenue = df.groupby("Date")['Revenue'].sum()
    plt.figure(figsize=(10,6))
    monthly_revenue.plot(kind='line', marker='o', color='navy')
    plt.title("Monthly Revenue Trend")
    plt.xlabel('Date')
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 2 Revenue by Product
def plot_revenue_by_product(df):
    product_revenue = df.groupby('Product')['Revenue'].sum()
    plt.figure(figsize=(8,6))
    product_revenue.plot(kind='bar', color='skyblue')
    plt.title('Revenue by Product')
    plt.ylabel('Total Revenue')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# 3 Revenue by Region
def plot_revenue_by_region(df):
    region_revenue = df.groupby('Region')['Revenue'].sum()
    plt.figure(figsize=(8,6))
    region_revenue.plot(kind='bar', color='seagreen')
    plt.title('Revenue by Region')
    plt.ylabel('Total Revenue')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# 4 Product Share of Total Revenue
def plot_product_share(df):
    product_share = df.groupby('Product')['Revenue'].sum()
    plt.figure(figsize=(7,7))
    product_share.plot(kind='pie', autopct='%1.1f%%', startangle=90, color=['gold','lightblue','lightgreen','salmon'])
    plt.title('Product Share of Total Revenue')
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

# 5 Product-Region Heatmap
def plot_product_region_heatmap(df):
    pivot = df.pivot_table(values='Revenue', index='Region', columns='Product', aggfunc='sum')
    plt.figure(figsize=(8,6))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="Blues")
    plt.title("Revenue by Product and Region")
    plt.tight_layout()
    plt.show()

# 6 Units Vs Revenue
def plot_units_vs_revenue(df):
    plt.figure(figsize=(8,6))
    for product in df['Product'].unique():
        subset = df[df['Product'] == product]
        plt.scatter(subset['Units_Sold'], subset['Revenue'], label=product, alpha=0.7)
    plt.title("Units Sold vs Revenue by product")
    plt.xlabel('Units Sold')
    plt.ylabel("Revenue")
    plt.legend(title='Product')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()    





plot_units_vs_revenue(df)
plot_revenue_by_product(df)
plot_revenue_trend(df)
plot_revenue_by_region(df)
plot_product_share(df)
plot_product_region_heatmap(df)

