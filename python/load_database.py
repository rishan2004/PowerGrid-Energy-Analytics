import pandas as pd
import sqlite3
import os

# --------------------------------------------------
# Load CSV
# --------------------------------------------------

csv_path = "data/electricity_data.csv"

df = pd.read_csv(csv_path)

df["timestamp"] = pd.to_datetime(df["timestamp"])

# --------------------------------------------------
# Create database
# --------------------------------------------------

db_path = "data/powergrid.db"

conn = sqlite3.connect(db_path)

# --------------------------------------------------
# Create table
# --------------------------------------------------

df.to_sql(
    "meter_readings",
    conn,
    if_exists="replace",
    index=False
)

# --------------------------------------------------
# Verify
# --------------------------------------------------

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM meter_readings"
)

count = cursor.fetchone()[0]

print("=" * 50)
print("POWERGRID SQL DATABASE")
print("=" * 50)

print(f"\nRecords inserted: {count:,}")

cursor.execute(
    "SELECT COUNT(DISTINCT meter_id) FROM meter_readings"
)

meters = cursor.fetchone()[0]

print(f"Meters: {meters}")

# --------------------------------------------------
# Close connection
# --------------------------------------------------

conn.close()

print(f"\nDatabase created: {db_path}")
print("Table created: meter_readings")