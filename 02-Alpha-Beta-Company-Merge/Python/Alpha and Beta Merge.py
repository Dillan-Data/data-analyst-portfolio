import pandas as pd

# ============================
# 1. LOAD RAW DATA
# ============================
alpha = pd.read_csv("Alpha Company Sales 2024 - Sheet1.csv")
beta = pd.read_csv("Beta Company Sales 2024 - Sheet1.csv")

# ============================
# 2. STANDARDIZE COLUMN NAMES
# ============================
alpha.columns = alpha.columns.str.lower().str.strip().str.replace(" ", "_")
beta.columns  = beta.columns.str.lower().str.strip().str.replace(" ", "_")

# --- After this, the names are:
# orderid, date, customer, product, quantity, unitprice, totalprice, currency

# ============================
# 3. CLEAN CURRENCY FIELDS
# ============================

def clean_currency(series):
    return (
        series.astype(str)
              .str.replace(r"[$€,]", "", regex=True)
              .astype(float)
    )

alpha["unitprice"]  = clean_currency(alpha["unitprice"])
alpha["totalprice"] = clean_currency(alpha["totalprice"])

beta["unitprice"]   = clean_currency(beta["unitprice"])
beta["totalprice"]  = clean_currency(beta["totalprice"])

# ============================
# 4. FIX DATE COLUMNS
# ============================
alpha["date"] = pd.to_datetime(alpha["date"], dayfirst=True)
beta["date"]  = pd.to_datetime(beta["date"], dayfirst=True)

# ============================
# 5. ADD COMPANY LABEL
# ============================
alpha["company"] = "Alpha"
beta["company"]  = "Beta"

# ============================
# 6. ADD CURRENCY CONVERSIONS
# ============================

usd_to_eur = 0.92
eur_to_usd = 1.09

# Alpha is USD
alpha["sales_usd"] = alpha["totalprice"]
alpha["sales_eur"] = alpha["totalprice"] * usd_to_eur

# Beta is EUR
beta["sales_eur"] = beta["totalprice"]
beta["sales_usd"] = beta["totalprice"] * eur_to_usd

# ============================
# 7. MERGE DATASETS
# ============================
merged = pd.concat([alpha, beta], ignore_index=True)

# ============================
# 8. SUMMARY KPIs
# ============================
summary = {
    "Total Sales USD (Alpha)": alpha["sales_usd"].sum(),
    "Total Sales USD (Beta conv)": beta["sales_usd"].sum(),
    "Total Combined USD": merged["sales_usd"].sum(),
    
    "Total Sales EUR (Alpha conv)": alpha["sales_eur"].sum(),
    "Total Sales EUR (Beta)": beta["sales_eur"].sum(),
    "Total Combined EUR": merged["sales_eur"].sum(),
    
    "Top Product by USD Sales": merged.groupby("product")["sales_usd"].sum().idxmax(),
    "Top Product by EUR Sales": merged.groupby("product")["sales_eur"].sum().idxmax(),
}

print("\n===== SUMMARY METRICS =====")
for k, v in summary.items():
    if isinstance(v, (int, float)):    
        print(f"{k}: {round(v, 2)}")
    else:
        print(f"{k}: {v}")

# ============================
# 9. EXPORT CLEAN FILES
# ============================
alpha.to_csv("Clean_Alpha_Sales.csv", index=False)
beta.to_csv("Clean_Beta_Sales.csv", index=False)
merged.to_csv("Merged_Alpha_Beta_Sales.csv", index=False)

print("\nFiles exported successfully.")

# === START: KPI + Text + PDF EXPORT SECTION ===
import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# Paths (adjust if you prefer different folder)
merged_csv_path = "Merged_Alpha_Beta_Sales.csv"   # final CSV you've exported
summary_txt_path = "Sales_Summary.txt"
summary_pdf_path = "Sales_Summary.pdf"
charts_dir = "kpi_charts"
os.makedirs(charts_dir, exist_ok=True)

# --- Safety: ensure merged exists; if not, try to load the CSV
if 'merged' not in globals():
    if os.path.exists(merged_csv_path):
        merged = pd.read_csv(merged_csv_path, parse_dates=['date'], dayfirst=True)
    else:
        raise RuntimeError("Merged dataframe not in memory and merged CSV not found.")

# Normalize product names (optional, helps grouping)
merged['product'] = merged['product'].astype(str).str.strip().str.title()

# Ensure numeric columns present and typed correctly
for col in ['sales_usd', 'sales_eur', 'quantity']:
    if col in merged.columns:
        merged[col] = pd.to_numeric(merged[col], errors='coerce').fillna(0)
    else:
        # attempt to compute from total columns if available
        if 'totalprice' in merged.columns and merged.get('currency', '').any():
            # best-effort: assume totalprice corresponds to native currency and conversions already exist
            merged[col] = 0

# Add convenient date parts
if 'date' in merged.columns:
    merged['date'] = pd.to_datetime(merged['date'], dayfirst=True, errors='coerce')
    merged['year'] = merged['date'].dt.year
    merged['month'] = merged['date'].dt.strftime('%Y-%m')
else:
    merged['date'] = pd.NaT
    merged['month'] = None

# ---- KPI CALCULATIONS ----

# Overall totals
alpha_usd = merged.loc[merged['company']=='Alpha','sales_usd'].sum()
beta_usd  = merged.loc[merged['company']=='Beta','sales_usd'].sum()
combined_usd = merged['sales_usd'].sum()

alpha_eur = merged.loc[merged['company']=='Alpha','sales_eur'].sum()
beta_eur  = merged.loc[merged['company']=='Beta','sales_eur'].sum()
combined_eur = merged['sales_eur'].sum()

# product KPIs
product_units = merged.groupby('product')['quantity'].sum().sort_values(ascending=False)
product_rev_usd = merged.groupby('product')['sales_usd'].sum().sort_values(ascending=False)
product_rev_eur = merged.groupby('product')['sales_eur'].sum().sort_values(ascending=False)

top_product_usd = product_rev_usd.idxmax() if not product_rev_usd.empty else None
top_product_eur = product_rev_eur.idxmax() if not product_rev_eur.empty else None
bottom_product_usd = product_rev_usd.idxmin() if not product_rev_usd.empty else None

# customer KPIs (if customer column exists)
unique_customers = merged['customer'].nunique() if 'customer' in merged.columns else 0
customer_rev = merged.groupby('customer')['sales_usd'].sum().sort_values(ascending=False)
top_customer = customer_rev.index[0] if not customer_rev.empty else None
avg_sale_per_customer = customer_rev.mean() if not customer_rev.empty else 0

# company comparison metrics
avg_sale_alpha = merged.loc[merged['company']=='Alpha','sales_usd'].mean()
avg_sale_beta = merged.loc[merged['company']=='Beta','sales_usd'].mean()
percent_diff_usd = ((alpha_usd - beta_usd) / beta_usd * 100) if beta_usd != 0 else float('inf')

# time-based KPIs
sales_by_date = merged.groupby('date')['sales_usd'].sum().dropna().sort_index()
best_day = sales_by_date.idxmax() if not sales_by_date.empty else None
worst_day = sales_by_date.idxmin() if not sales_by_date.empty else None

# Compose KPI dictionary (for printing & report)
kpis = {
    "Total Sales USD (Alpha)": alpha_usd,
    "Total Sales USD (Beta, converted)": beta_usd,
    "Total Combined USD": combined_usd,
    "Total Sales EUR (Alpha, converted)": alpha_eur,
    "Total Sales EUR (Beta)": beta_eur,
    "Total Combined EUR": combined_eur,
    "Top Product (by USD revenue)": top_product_usd,
    "Top Product (by EUR revenue)": top_product_eur,
    "Bottom Product (by USD revenue)": bottom_product_usd,
    "Unique Customers": unique_customers,
    "Top Customer (USD)": top_customer,
    "Average Sale per Customer (USD)": avg_sale_per_customer,
    "Average Sale Value Alpha (USD)": avg_sale_alpha,
    "Average Sale Value Beta (USD)": avg_sale_beta,
    "Percent Difference Alpha vs Beta (USD)": percent_diff_usd,
    "Best Sales Day (USD)": best_day,
    "Worst Sales Day (USD)": worst_day,
}

# ---- PRINT KPIs TO CONSOLE ----
print("\n===== KPI SUMMARY =====")
for k, v in kpis.items():
    if isinstance(v, (int, float)):
        if pd.isna(v) or v==float('inf'):
            print(f"{k}: N/A")
        else:
            print(f"{k}: {round(v, 2)}")
    else:
        print(f"{k}: {v}")

# ---- WRITE KPIS TO TEXT FILE ----
with open(summary_txt_path, "w", encoding="utf-8") as f:
    f.write("Merged Company Sales Analysis - KPI Summary\n")
    f.write(f"Generated: {datetime.now().isoformat()}\n\n")
    for k, v in kpis.items():
        if isinstance(v, (int, float)):
            if pd.isna(v) or v==float('inf'):
                f.write(f"{k}: N/A\n")
            else:
                f.write(f"{k}: {round(v, 2)}\n")
        else:
            f.write(f"{k}: {v}\n")

    # small tables
    f.write("\n\nTop Products by USD Revenue:\n")
    f.write(product_rev_usd.head(10).to_string())
    f.write("\n\nUnits sold by Product:\n")
    f.write(product_units.to_string())
    f.write("\n\nSales by Date (USD) - sample:\n")
    f.write(sales_by_date.head(20).to_string())

print(f"\n✅ Text summary saved to: {summary_txt_path}")

# ---- MAKE SIMPLE CHARTS (PNG) ----
# Product revenue chart (top 6)
plt.figure(figsize=(8,4))
top6 = product_rev_usd.head(6)
top6.plot(kind='bar')
plt.title("Top 6 Products by USD Revenue")
plt.ylabel("Revenue (USD)")
plt.tight_layout()
prod_chart = os.path.join(charts_dir, "top_products_usd.png")
plt.savefig(prod_chart)
plt.close()

# Sales over time chart (daily)
plt.figure(figsize=(10,4))
sales_by_date.plot(kind='line', marker='o')
plt.title("Daily Sales (USD)")
plt.ylabel("Revenue (USD)")
plt.tight_layout()
time_chart = os.path.join(charts_dir, "sales_over_time_usd.png")
plt.savefig(time_chart)
plt.close()

# ---- BUILD A SIMPLE PDF USING fpdf ----
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 8, "Merged Company Sales Analysis - 2024", ln=1, align="C")
        self.ln(2)

pdf = PDFReport()
pdf.set_auto_page_break(auto=True, margin=12)
pdf.add_page()

# Executive summary block
pdf.set_font("Arial", "", 11)
pdf.multi_cell(0, 6, "Executive Summary:\nThis report presents a combined sales analysis for Alpha (USD) and Beta (EUR) for 2024. "
                    "Currency conversions used: 1 USD = 0.92 EUR, 1 EUR = 1.09 USD. The table below shows top-line KPIs.")
pdf.ln(4)

# KPIs printed in bold label + value rows
pdf.set_font("Arial", "B", 11)
for k, v in kpis.items():
    pdf.set_font("Arial", "B", 11)
    pdf.cell(80, 6, str(k), border=0)
    pdf.set_font("Arial", "", 11)
    # format numeric nicely
    if isinstance(v, (int, float)) and not pd.isna(v) and v!=float('inf'):
        val = f"{round(v,2):,}"
    else:
        val = str(v)
    pdf.cell(0, 6, val, ln=1)

pdf.add_page()
# Insert product chart
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 6, "Top Products (USD)", ln=1)
pdf.image(prod_chart, w=170)
pdf.ln(4)

pdf.add_page()
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 6, "Sales Over Time (USD)", ln=1)
pdf.image(time_chart, w=170)
pdf.ln(4)

# Appendix tables - small samples
pdf.add_page()
pdf.set_font("Arial", "B", 12)
pdf.cell(0,6,"Product Revenue (Top 10) - USD", ln=1)
pdf.set_font("Arial", "", 10)
# Add a few rows from product_rev_usd
for prod, rev in product_rev_usd.head(10).items():
    pdf.cell(120,5,str(prod), border=0)
    pdf.cell(0,5,f"{round(rev,2):,}", ln=1)

# Save PDF
pdf.output(summary_pdf_path)
print(f"✅ PDF summary saved to: {summary_pdf_path}")

# Optionally re-export merged to a definitive path (already done earlier)
merged.to_csv(merged_csv_path, index=False)
print(f"✅ Merged CSV exported to: {merged_csv_path}")

# === END: KPI + Text + PDF EXPORT SECTION ===

