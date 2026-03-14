import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- GLOBAL THEME SETTINGS ---
palette_main = ["#234F32", "#2A9D8F", "#E9C46A", "#F4A261", "#E76F51"]

sns.set_theme(
    style="whitegrid",
    rc={
        "axes.titlesize": 18,
        "axes.labelsize": 14,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "font.family": "Segoe UI",
    }
)

sns.set_palette(palette_main)

def style_axes(ax):
    ax.title.set_color("#234F32")
    ax.xaxis.label.set_color("#4A4A4A")
    ax.yaxis.label.set_color("#4A4A4A")
    ax.tick_params(colors="#4A4A4A")

# --- LOAD DATA ---
df = pd.read_csv(r'G:\Data Analysis Portfolio\Biodiversity in National Parks\DATA CLEANED\species_observations_merged.csv')

# --- VISUAL 1 ---
category_risk = df.groupby("category")["is_protected"].mean().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10,6))
sns.barplot(data=category_risk, x='category', y='is_protected')
plt.title("Proportion of Protected Species by Category")
plt.ylabel("Protection Rate")
plt.xlabel("Species Category")
plt.xticks(rotation=45)
style_axes(plt.gca())
plt.tight_layout()
plt.savefig("chart_category_risk.png", dpi=300, bbox_inches="tight")
plt.show()

# --- VISUAL 2 ---
park_protection = df.groupby(['park_name', 'is_protected'])['observations'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(data=park_protection, x='park_name', y='observations', hue='is_protected')
plt.title("Protected vs Non-Protected Observations by Park")
plt.xticks(rotation=45)
style_axes(plt.gca())
plt.tight_layout()
plt.savefig("chart_park_protection.png", dpi=300, bbox_inches="tight")
plt.show()

# --- VISUAL 3 ---
protected_counts = (
    df[df['is_protected']]
    .groupby('category')['scientific_name']
    .nunique()
    .reset_index(name='protected_species')
    .sort_values('protected_species', ascending=False)
)

plt.figure(figsize=(10,6))
sns.barplot(data=protected_counts, x='category', y='protected_species')
plt.title("Number of Protected Species by Category")
plt.xlabel("Species Category")
plt.ylabel("Protected Species Count")
plt.xticks(rotation=45)
style_axes(plt.gca())
plt.tight_layout()
plt.savefig("chart_protected_species_count.png", dpi=300, bbox_inches="tight")
plt.show()

# --- VISUAL 4 ---
protected_parks = (
    df[df['is_protected']]
    .groupby('park_name')['observations']
    .sum()
    .reset_index()
    .sort_values('observations', ascending=False)
)

plt.figure(figsize=(10,6))
sns.barplot(data=protected_parks, x='park_name', y='observations')
plt.title('Protected Species Observations by Park')
plt.xlabel("Park")
plt.ylabel('Observation Count')
plt.xticks(rotation=45)
style_axes(plt.gca())
plt.tight_layout()
plt.savefig("chart_protected_parks.png", dpi=300, bbox_inches="tight")
plt.show()

# --- VISUAL 5 ---
top_species = (
    df[df['is_protected']]
    .groupby('common_names')['observations']
    .sum()
    .reset_index()
    .sort_values('observations', ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
sns.barplot(data=top_species, y='common_names', x='observations')
plt.title("Top Observed Protected Species")
plt.xlabel('Observations')
plt.ylabel('Species')
style_axes(plt.gca())
plt.tight_layout()
plt.savefig("chart_top_observed_protected_species.png", dpi=300, bbox_inches="tight")
plt.show()

# --- VISUAL 6 ---
category_protection = df.groupby('category')['is_protected'].mean().reset_index()
category_protection["protection_rate"] = category_protection['is_protected'] * 100

plt.figure(figsize=(10,6))
sns.barplot(data=category_protection, x='category', y='protection_rate')
plt.title('Percentage of Species Under Protection by Category')
plt.ylabel("Protection Rate (%)")
plt.xlabel("Species Category")
plt.xticks(rotation=45)
style_axes(plt.gca())
plt.tight_layout()
plt.savefig('chart_protection_rate_percentage.png', dpi=300, bbox_inches="tight")
plt.show()

# --- VISUAL 7 ---
status_distribution = (
    df.groupby('conservation_status')['scientific_name']
    .nunique()
    .reset_index(name='species_count')
    .sort_values('species_count', ascending=False)
)

plt.figure(figsize=(10,6))
sns.barplot(data=status_distribution, x='conservation_status', y='species_count')
plt.title("Distribution of Conservation Status Across Species")
plt.ylabel('Number of Species')
plt.xlabel('Conservation Status')
plt.xticks(rotation=45)
style_axes(plt.gca())
plt.tight_layout()
plt.savefig('chart_conservation_status_distribution.png', dpi=300, bbox_inches="tight")
plt.show()

