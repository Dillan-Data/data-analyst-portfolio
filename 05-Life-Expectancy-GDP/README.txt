Life Expectancy & GDP Analysis

Exploratory Data Analysis & Visualization in Python

Overview

This project explores the relationship between economic output (GDP) and life expectancy across multiple countries over time. Using publicly available data from the World Bank and World Health Organization, the analysis focuses on identifying trends, relationships, and limitations through clear and interpretable data visualizations.

The project was completed as part of the Codecademy Data Scientist: Analytics career path and is designed to demonstrate practical skills in data wrangling, exploratory data analysis, and data visualization.

Objectives

Explore how life expectancy has changed over time by country

Analyze GDP trends and compare growth patterns across countries

Investigate the relationship between GDP and life expectancy

Communicate insights using effective visualizations

Practice presenting data-driven conclusions clearly and professionally

Dataset

Source: World Bank & World Health Organization

File: all_data.csv

Key columns:

Country

Year

GDP

Life expectancy at birth (years)

Tools & Technologies

Python

Pandas – data manipulation

Matplotlib & Seaborn – data visualization

Jupyter Notebook / Python script

Data Preparation

Key preprocessing steps:

Renamed columns for readability (life_expectancy, gdp)

Removed missing values

Verified data types and value ranges

Applied log scaling to GDP for meaningful comparison

Visualizations

The following visualizations were created to answer the research questions:

Violin Plot – Life Expectancy by Country
Displays the distribution and variability of life expectancy across countries.

Facet Scatter Plots – GDP vs Life Expectancy
Shows the relationship between economic output and longevity using a logarithmic GDP scale.

Facet Line Plots – GDP Over Time
Highlights economic growth patterns and volatility by country.

Facet Line Plots – Life Expectancy Over Time
Illustrates long-term health improvements and cross-country differences.

Key Insights

Higher GDP is generally associated with higher life expectancy.

The relationship between GDP and life expectancy shows diminishing returns at higher income levels.

Life expectancy has increased over time even in countries with slower GDP growth.

Economic growth alone does not fully explain health outcomes—policy, healthcare, and social factors matter.

Limitations

GDP is an aggregate metric and does not account for income inequality.

Other influential variables (education, healthcare spending, conflict) are not included.

The dataset focuses on a limited set of countries.

Future Improvements

Add correlation and regression analysis

Include additional socioeconomic indicators

Extend the analysis to more countries or regions

Build an interactive dashboard (Power BI or Tableau)

Project Context

This project was completed as part of a Codecademy portfolio requirement and reflects a learning-focused but production-quality approach to exploratory data analysis and visualization.

Author

Dillan
Aspiring Data Analyst / Data Scientist
Focused on practical analytics, visualization, and business-oriented insights