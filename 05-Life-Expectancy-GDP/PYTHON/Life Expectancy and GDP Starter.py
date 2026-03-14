#How has life expectancy changed over time for each country?
#How has GDP changed over time for each country?
#Is there a relationship between GDP and life expectancy?
#Does that relationship differ by country?
#Has the GDP–life expectancy relationship strengthened over time?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('G:\\Data Analysis Portfolio\\Life-Expectancy-and-GDP-Starter\\all_data.csv')

#print(df.head())
#print(df.info())
#print(df.describe())

# Rename comlumns
df = df.rename(columns={
    "Life expectancy at birth (years)": "life_expectancy",
    "GDP": "gdp"
})

# Check for missing values
df.isna().sum()

#drop missing values
df = df.dropna()

#print(df.head())

# Exploratory Analysis
# Life Expectancy by Country
df.groupby("Country")['life_expectancy'].mean().sort_values()

# GPD by Country
df.groupby('Country')['gdp'].mean().sort_values()

# Visualizations
# Life Expectancy over time
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='Year', y='life_expectancy', hue='Country')
plt.title('Life Expectancy Over Time By Country')
plt.ylabel('Life Expectancy (Years)')
plt.xlabel('Years')
plt.show()

# GDP Over Time
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='Year', y='gdp', hue='Country')
plt.yscale('log')
plt.title("GDP Over Time By Country (Log Scale)")
plt.ylabel('GDP (log Scale)')
plt.xlabel("Year")
plt.show()


# GDP vs Life Expectancy
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='gdp', y='life_expectancy', hue='Country')
plt.xscale('log')
plt.title('GDP vs Life Expectancy')
plt.xlabel('GDP (log scale)')
plt.ylabel('Life Expectancy')
plt.show()

# Is Wealth Associated with Longer Life?
sns.lmplot(
    data=df,
    x="gdp",
    y="life_expectancy",
    hue="Country",
    height=6,
    aspect=1.2,
    scatter_kws={"alpha":0.5},
    logx=True
)
plt.title("GDP vs Life Expectancy with Trend Lines")
plt.show()
