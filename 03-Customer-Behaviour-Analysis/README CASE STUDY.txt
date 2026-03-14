Case Study: Online Retail Sales, Customer & Operational Analysis
1. Background & Problem Statement

The business operates an online retail platform selling physical products to customers across multiple countries. Transaction-level data is available, including product details, customer IDs, timestamps, and returns.

The core problem is lack of visibility:

Sales totals exist, but trends are unclear

Customer behavior is not well understood

Product returns are impacting revenue, but the causes are unknown

Operational timing (when orders happen) is not being leveraged

The objective of this project was to turn raw transactional data into decision-ready insights using Python for analysis and Power BI for reporting.

2. Data Understanding

The dataset contains individual invoice line items with:

Invoice number and timestamp (to the minute)

Product identifiers and descriptions

Quantity and unit price

Customer ID

Country

Important characteristics identified early:

Returns are represented as negative quantities

Sales data is highly skewed (few large customers, many small ones)

Time information is granular enough to analyze hourly and weekday behavior

Understanding these characteristics upfront shaped the entire analysis approach.

3. Data Cleaning & Preparation (Python)
Key Decisions

Cleaning was isolated into a single dedicated script

All analysis was performed on a cleaned dataset only

Consistent naming (snake_case) was enforced to prevent downstream errors

Key Transformations

Parsed invoice timestamps into datetime format

Removed invalid or incomplete records

Created derived features:

total_sales (quantity × unit price)

is_return flag for negative quantities

abs_quantity for volume analysis

Time features (year, month, weekday, hour)

Why this mattered

Separating cleaning from analysis prevented logic errors and allowed:

Reliable reuse of the cleaned dataset

Easier debugging

Clean handoff to Power BI

This step formed the foundation of the entire project.

4. Sales Performance Analysis
Questions Asked

How much revenue is generated overall?

How much is lost to returns?

How does sales performance change over time?

Which countries drive the most revenue?

Key Findings

Net sales are significantly lower than gross sales due to returns

Sales exhibit clear monthly patterns, indicating seasonality

Revenue is heavily concentrated in a small number of countries

Insight

Looking only at total sales hides volatility and risk. Net sales and trends provide a much more realistic picture of business health.

5. Customer Behavior Analysis
Questions Asked

How many customers are there?

How often do they buy?

How evenly is revenue distributed across customers?

Key Findings

Customer spend distribution is highly right-skewed

Median customer spend is far lower than the mean

A small number of customers contribute a disproportionate share of revenue

Insight

The business is exposed to customer concentration risk. Losing a few high-value customers would materially impact revenue.

This insight is not visible without aggregating at the customer level.

6. Product & Returns Analysis
Questions Asked

Which products generate the most revenue?

Which products are returned most frequently?

Are high-selling products also high-return products?

Key Findings

Some products sell in high volume but contribute less revenue

Certain products have disproportionately high return rates

Returns are not evenly distributed across the product catalog

Insight

Returns are a product-specific problem, not a general one. Targeted quality or logistics interventions would likely reduce revenue loss more effectively than broad policies.

7. Operational & Time-Based Insights
Questions Asked

When do customers place orders?

Are there clear peak hours or peak days?

When do returns tend to occur?

Key Findings

Orders cluster around specific hours of the day

Certain weekdays consistently show higher order volume

Returns show temporal patterns that may align with delivery cycles

Insight

Operational decisions (staffing, promotions, customer support availability) can be optimized using time-based sales behavior instead of intuition.

8. Power BI Dashboard

The final insights were presented in a three-page Power BI dashboard:

Executive Overview
High-level KPIs and sales trends for decision-makers

Customer & Product Insights
Deep dive into who buys and what sells (and returns)

Operational Insights
Time-based patterns relevant to operations and logistics

Interactive filters allow stakeholders to explore the data by country, month, and year.

9. What I Learned From This Project

Separating data cleaning and analysis is critical

Naming consistency prevents most debugging issues

Asking the right business questions matters more than fancy visuals

A clean dashboard is a communication tool, not a data dump

End-to-end projects are far more valuable than isolated scripts

10. Outcome

This project demonstrates the full data analysis lifecycle:

Raw data → clean dataset

Clean dataset → structured analysis

Analysis → actionable insights

Insights → business-ready dashboard

It serves as both a learning milestone and a client-ready portfolio piece.