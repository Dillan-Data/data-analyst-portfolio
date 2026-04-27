Online Retail Sales Analysis & Customer Insights
Project Overview

This project analyzes online retail transaction data to uncover insights into sales performance, customer behavior, product performance, returns, and operational trends.
The goal is to demonstrate an end-to-end data analysis workflow — from raw data cleaning in Python to interactive business intelligence reporting in Power BI.

The analysis is structured to answer questions a real business would ask when optimizing revenue, operations, and customer strategy.

Dataset

Source: Online Retail transactional dataset

Granularity:

Individual invoice line items

Timestamped to the minute

Multiple countries and customers

Key Fields:

Invoice Number & Date

Product (StockCode, Description)

Quantity & Unit Price

Customer ID

Country

The dataset includes both completed sales and returned items, allowing for return rate analysis and operational insights.

Tools & Technologies

Python

pandas

numpy

datetime

Power BI

DAX measures

Interactive dashboards

KPI cards and time-based visuals

Data Preparation & Feature Engineering

Data cleaning and transformation were performed in Python, including:

Handling missing values and invalid transactions

Parsing invoice timestamps

Creating new analytical features:

total_sales

is_return

abs_quantity

Time features (year, month, month name, weekday, hour)

Exporting a clean, analysis-ready dataset for Power BI

This ensured consistent logic between Python analysis and BI reporting.

Key Analyses & Insights
1. Sales Performance

Total and net sales tracking

Monthly sales trends and seasonality

Sales distribution across countries

Impact of returns on revenue

2. Customer & Product Insights

Total customers and order volume

Top-selling products

Product return behavior

Customer purchasing patterns

3. Products & Returns

Identification of high-return products

Return rate calculation

Revenue loss due to returns

4. Operational & Time-Based Insights

Orders by day of week

Orders by hour of day

Peak sales periods

Operational timing patterns useful for staffing and marketing decisions

Power BI Dashboard

An interactive Power BI report was created with three main pages:

Sales Performance Overview

KPIs (Total Sales, Net Sales, Orders, Customers, Return Rate)

Monthly trends and country comparisons

Customer & Product Insights

Product performance

Customer distribution

Return behavior by product

Operational & Time-Based Insights

Order volume by weekday and hour

Time-based sales and return trends

The dashboard allows filtering by country, month, and year to explore different business perspectives.

Deliverables

Cleaned and feature-engineered dataset (online_retail_cleaned.csv)

Python analysis scripts

Interactive Power BI dashboard

PDF summary report

Dashboard screenshots for portfolio use
![Project Visual](<IMAGES/Customer Purchase Behavior & Sampling Analysis_pages-to-jpg-0001.jpg>)
![Project Visual](<IMAGES/Customer Purchase Behavior & Sampling Analysis_pages-to-jpg-0002.jpg>)
![Project Visual](<IMAGES/Customer Purchase Behavior & Sampling Analysis_pages-to-jpg-0003.jpg>)

This analysis is relevant for:

E-commerce performance reporting

Sales and operations teams

Customer behavior analysis

Business intelligence portfolio demonstrations
