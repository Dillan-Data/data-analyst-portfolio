import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(
    r'G:\Data Analysis Portfolio\Customer Purchase Behavior & Sampling Analysis\DATA\online_retail.csv',
    encoding='ISO-8859-1'
)

def clean_online_retail(df):
    """
    Cleaning pipeline tailored for Online Retail sales data.
    """

    # 1. Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # 2. Remove duplicate rows
    df = df.drop_duplicates()
    df = df.rename(columns={'invoicedate': 'invoice_date'})
    # 3. Convert invoice_date to datetime
    df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')

    # Drop rows with invalid dates
    df = df.dropna(subset=['invoice_date'])

    # 4. Handle missing customer IDs
    # Keep them, but label as unknown (important for retail analysis)
    df['customerid'] = df['customerid'].fillna('unknown')

    # 5. Ensure numeric columns are correct
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['unitprice'] = pd.to_numeric(df['unitprice'], errors='coerce')

    # Drop rows with invalid pricing
    df = df.dropna(subset=['quantity', 'unitprice'])

    # 6. Create business-critical features
    df['total_sales'] = df['quantity'] * df['unitprice']

    # Flag returns (negative quantity)
    df['is_return'] = df['quantity'] < 0

    # Absolute quantity for analysis
    df['abs_quantity'] = df['quantity'].abs()

    # 7. Time-based features (for Power BI & EDA)
    df['year'] = df['invoice_date'].dt.year
    df['month'] = df['invoice_date'].dt.month
    df['month_name'] = df['invoice_date'].dt.month_name()
    df['day'] = df['invoice_date'].dt.day
    df['hour'] = df['invoice_date'].dt.hour
    df['weekday'] = df['invoice_date'].dt.day_name()

    # 8. Clean text columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip().str.lower()

    return df

# Apply cleaning
df_clean = clean_online_retail(df)

# Preview cleaned data
print(df_clean.head())
print(df_clean.info())

df_clean.to_csv("online_retail_cleaned.csv", index=False)

# DATASET OVERVIEW (use df_clean ONLY)
overview = {
    "date_range": (
        df_clean["invoice_date"].min(),
        df_clean["invoice_date"].max()
    ),
    "total_transactions": df_clean["invoiceno"].nunique(),
    "total_customers": df_clean["customerid"].nunique(),
    "total_products": df_clean["stockcode"].nunique(),
    "countries": df_clean["country"].nunique(),
    "gross_sales": df_clean.loc[~df_clean["is_return"], "total_sales"].sum(),
    "total_returns": df_clean.loc[df_clean["is_return"], "total_sales"].sum(),
    "net_sales": df_clean["total_sales"].sum()
}

for k, v in overview.items():
    print(f"{k}: {v}")



