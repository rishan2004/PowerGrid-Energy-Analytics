import sqlite3
import pandas as pd

db_path = "data/powergrid.db"

conn = sqlite3.connect(db_path)

print("=" * 60)
print("POWERGRID SQL ANALYTICS")
print("=" * 60)


# --------------------------------------------------
# 1. Total Energy
# --------------------------------------------------

query = """
SELECT
    ROUND(SUM(energy_kwh), 2) AS total_energy_kwh
FROM meter_readings;
"""

result = pd.read_sql_query(query, conn)

print("\n1. TOTAL ENERGY")
print(result)


# --------------------------------------------------
# 2. Average & Peak Power
# --------------------------------------------------

query = """
SELECT
    ROUND(AVG(power_kw), 2) AS average_power_kw,
    ROUND(MAX(power_kw), 2) AS peak_demand_kw
FROM meter_readings;
"""

result = pd.read_sql_query(query, conn)

print("\n2. POWER STATISTICS")
print(result)


# --------------------------------------------------
# 3. Meter Performance
# --------------------------------------------------

query = """
SELECT
    meter_id,
    ROUND(SUM(energy_kwh), 2) AS total_energy_kwh,
    ROUND(AVG(power_kw), 2) AS average_power_kw,
    ROUND(MAX(power_kw), 2) AS peak_power_kw,
    ROUND(AVG(power_factor), 3) AS average_power_factor
FROM meter_readings
GROUP BY meter_id
ORDER BY total_energy_kwh DESC;
"""

result = pd.read_sql_query(query, conn)

print("\n3. METER PERFORMANCE")
print(result)


# --------------------------------------------------
# 4. Hourly Load
# --------------------------------------------------

query = """
SELECT
    CAST(strftime('%H', timestamp) AS INTEGER) AS hour,
    ROUND(AVG(power_kw), 2) AS average_load_kw
FROM meter_readings
GROUP BY hour
ORDER BY average_load_kw DESC;
"""

result = pd.read_sql_query(query, conn)

print("\n4. PEAK HOURS")
print(result.head(5))


# --------------------------------------------------
# 5. High Consumption Events
# --------------------------------------------------

query = """
SELECT
    meter_id,
    timestamp,
    ROUND(power_kw, 2) AS power_kw
FROM meter_readings
WHERE power_kw > 110
ORDER BY power_kw DESC
LIMIT 10;
"""

result = pd.read_sql_query(query, conn)

print("\n5. HIGH CONSUMPTION EVENTS")
print(result)


conn.close()

print("\nSQL ANALYSIS COMPLETED.")