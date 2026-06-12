import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv("NGO_Impact_Data.csv")

# Create database
conn = sqlite3.connect("NGO_Project.db")

# Create table and import data
df.to_sql(
    "ngo_impact_data",
    conn,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")

conn.close()