import pandas as pd

# Load dataset
df = pd.read_csv("NGO_Impact_Data.csv")

print("Dataset Loaded Successfully")
print("\n")

# Basic Information
print("Dataset Information")
print(df.info())

print("\n")

# First 5 Rows
print("First 5 Rows")
print(df.head())

print("\n")

# Missing Values
print("Missing Values")
print(df.isnull().sum())

print("\n")

# Duplicate Records
duplicates = df.duplicated().sum()

print("Duplicate Records:")
print(duplicates)

print("\n")

# Remove Duplicates
df = df.drop_duplicates()

# Validate Age
invalid_age = df[
    (df["Age"] < 18) |
    (df["Age"] > 45)
]

print("Invalid Age Records:")
print(len(invalid_age))

print("\n")

# Validate Scores
invalid_scores = df[
    (df["Pre_Assessment_Score"] < 0) |
    (df["Pre_Assessment_Score"] > 100) |
    (df["Post_Assessment_Score"] < 0) |
    (df["Post_Assessment_Score"] > 100)
]

print("Invalid Score Records:")
print(len(invalid_scores))

print("\n")

# Save Clean Dataset
df.to_csv(
    "NGO_Impact_Data_Cleaned.csv",
    index=False
)

print("Cleaned Dataset Saved Successfully!")