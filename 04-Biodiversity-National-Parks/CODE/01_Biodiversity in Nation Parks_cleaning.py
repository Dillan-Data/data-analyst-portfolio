# ===============================
# IMPORT LIBRARIES
# ===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ===============================
# LOAD DATA
# ===============================
species = pd.read_csv(
    r'G:\Data Analysis Portfolio\Biodiversity in National Parks\Biodiversity_starter\species_info.csv'
)

observations = pd.read_csv(
    r'G:\Data Analysis Portfolio\Biodiversity in National Parks\Biodiversity_starter\observations.csv'
)


# ===============================
# INITIAL INSPECTION
# ===============================
print("Species Shape:", species.shape)
print("Observations Shape:", observations.shape)

print(species.info())
print(observations.info())


# ===============================
# CLEAN SPECIES DATASET
# ===============================

# Standardize column names
species.columns = (
    species.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Strip whitespace from text columns
for col in ['category', 'scientific_name', 'common_names', 'conservation_status']:
    species[col] = species[col].astype(str).str.strip()

# Replace empty strings with NaN
species = species.replace({"": np.nan, "nan": np.nan})

# Remove trailing commas in names
species["common_names"] = species["common_names"].str.rstrip(",")

# IMPORTANT: Fill missing conservation status
species["conservation_status"] = species["conservation_status"].fillna(
    "No Intervention"
)

# Remove duplicate species
species = species.drop_duplicates(subset="scientific_name")

# Create protection flag (CRITICAL FOR ANALYSIS)
species["is_protected"] = (
    species["conservation_status"] != "No Intervention"
)


# ===============================
# CLEAN OBSERVATIONS DATASET
# ===============================

observations.columns = (
    observations.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Strip whitespace from object columns
for col in observations.columns:
    if observations[col].dtype == "object":
        observations[col] = observations[col].str.strip()

# Ensure observations column is numeric
observations["observations"] = pd.to_numeric(
    observations["observations"], errors="coerce"
)


# ===============================
# MERGE DATASETS
# ===============================

merged = observations.merge(
    species,
    on="scientific_name",
    how="left"
)


# ===============================
# VALIDATION CHECKS
# ===============================

print("\n--- Validation ---")
print("Species rows:", species.shape[0])
print("Observations rows:", observations.shape[0])
print("Merged rows:", merged.shape[0])

print("\nMissing values after merge:")
print(merged.isna().sum())


# ===============================
# EXPORT CLEAN DATA
# ===============================

species.to_csv("species_clean.csv", index=False)
observations.to_csv("observations_clean.csv", index=False)
merged.to_csv("species_observations_merged.csv", index=False)

print("\nFiles exported successfully.")