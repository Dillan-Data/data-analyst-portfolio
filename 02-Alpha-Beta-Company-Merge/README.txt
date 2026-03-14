📊 Merged Sales Analysis — Alpha & Beta Companies (2024)

Prepared by: Dillan Maart
Tools Used: Python, Pandas, Matplotlib, FPDF
Files Included:

Alpha Company Sales 2024.csv

Beta Company Sales 2024.csv

Merged_Alpha_Beta_Sales.csv

Sales_Summary.txt

Sales_Summary.pdf

Alpha_and_Beta_Merge.py

🧩 Project Overview

Alpha (USA-based, USD) and Beta (EU-based, EUR) merged operations in 2024. Each company historically kept separate sales data using different currencies, formats, and conventions.

This project consolidates both datasets into a single, cleaned, currency-standardized master file, and produces a full analytical report with KPIs, trends, and product performance insights.

Everything was done using pure Python, no Excel, no BI tools.
Just clean, efficient data engineering and analysis.

🎯 Objectives

Import and clean Alpha and Beta sales datasets.

Standardize all monetary values (USD ↔ EUR) using fixed conversion rates:

1 USD → 0.92 EUR

1 EUR → 1.09 USD

Merge both datasets into a single unified 2024 sales file.

Generate key KPIs needed by management.

Produce client-ready outputs:

Clean CSV

KPI summary text

Multi-page PDF report with charts

🛠️ Methods Used
✔️ Data Cleaning & Standardization

Removed currency symbols ($, €)

Converted string values to numeric

Standardized product names

Converted USD ↔ EUR

Added computed columns:

sales_usd

sales_eur

company

date, month, year

✔️ Merging & Transformation

Concatenated Alpha + Beta datasets

Ensured consistent schema across both

Derived KPIs from merged dataframe

✔️ KPI Computation

Includes (but not limited to):

Total sales (USD & EUR) for each company

Combined total revenue

Top-selling product

Bottom-selling product

Customer-level revenue contribution

Best/worst sales day

Average sale values

Product revenue rankings

Sales trends over time

✔️ Visualization & Reporting

Generated using Matplotlib:

Top products (USD revenue)

Sales over time

Generated using FPDF:

Multi-page PDF report

Executive Summary

KPI table

Embedded charts

Appendix tables

📁 Outputs
📄 1. Final Cleaned Dataset

Merged_Alpha_Beta_Sales.csv
Contains:

60 total transactions

Full currency conversions

Standardized product names

Uniform schema

Ready for BI dashboards or further analysis

📝 2. Text Summary Report

Sales_Summary.txt
Plain-text KPI summary for quick review.

📘 3. PDF Report

Sales_Summary.pdf
Includes:

Executive Summary

Full KPI Table

Charts

Appendix with product-level metrics

🧪 4. Full Python Script

Alpha_and_Beta_Merge.py
End-to-end ETL + EDA workflow:

Import

Clean

Merge

Convert currencies

Compute KPIs

Generate PDF

Export CSV

🔍 Key Insights (from the analysis)

(Adjust these once you review your real outputs.)

Alpha and Beta show strong complementary product strengths.

Revenue distribution shows clear top performers (input real product names).

The merged company benefits from cross-regional customer diversity.

Sales trends indicate optimal sales windows around X–Y dates.

Clear winner for Top Customer and highest revenue product category.

🚀 Future Enhancements

To further strengthen this project, possible improvements include:

Power BI dashboard

Forecasting model (Prophet / ARIMA)

Product profitability module

Customer segmentation

Currency conversion using real historical FX rates

💼 Contact

If you’d like a custom sales consolidation, dashboard, or reporting solution:

Dillan Maart — Data Analyst
Fiverr: https://www.fiverr.com/s/BRvWKm1
LinkedIn: https://www.linkedin.com/in/dillan-maart-091976171
Email: dillanmaart.freelancer@gmail.com