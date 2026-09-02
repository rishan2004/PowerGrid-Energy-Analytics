import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DB_PATH = os.path.join(
    BASE_DIR,
    "data",
    "powergrid.db"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "dashboard"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)


# ==================================================
# 1. EXECUTIVE SUMMARY
# ==================================================

summary_query = """
SELECT
    ROUND(SUM(energy_kwh), 2) AS total_energy_kwh,
    ROUND(AVG(power_kw), 2) AS average_power_kw,
    ROUND(MAX(power_kw), 2) AS peak_demand_kw,
    ROUND(AVG(power_factor), 3) AS average_power_factor,
    ROUND(AVG(voltage), 2) AS average_voltage,
    ROUND(AVG(current), 2) AS average_current
FROM meter_readings;
"""

summary = pd.read_sql_query(
    summary_query,
    conn
)

summary.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "executive_summary.csv"
    ),
    index=False
)


# ==================================================
# 2. METER PERFORMANCE
# ==================================================

meter_query = """
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

meter_data = pd.read_sql_query(
    meter_query,
    conn
)

meter_data.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "meter_performance.csv"
    ),
    index=False
)


# ==================================================
# 3. HOURLY LOAD
# ==================================================

hourly_query = """
SELECT
    CAST(strftime('%H', timestamp) AS INTEGER) AS hour,
    ROUND(AVG(power_kw), 2) AS average_load_kw,
    ROUND(MAX(power_kw), 2) AS peak_load_kw
FROM meter_readings
GROUP BY hour
ORDER BY hour;
"""

hourly_data = pd.read_sql_query(
    hourly_query,
    conn
)

hourly_data.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "hourly_load.csv"
    ),
    index=False
)


# ==================================================
# 4. ELECTRICAL METRICS
# ==================================================

electrical_query = """
SELECT
    meter_id,
    ROUND(AVG(voltage), 2) AS avg_voltage,
    ROUND(AVG(current), 2) AS avg_current,
    ROUND(AVG(power_factor), 3) AS avg_power_factor,
    ROUND(AVG(power_kw), 2) AS avg_real_power,
    ROUND(AVG(power_kw / power_factor), 2) AS avg_apparent_power
FROM meter_readings
GROUP BY meter_id;
"""

electrical_data = pd.read_sql_query(
    electrical_query,
    conn
)

electrical_data.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "electrical_metrics.csv"
    ),
    index=False
)


# ==================================================
# 5. ANOMALIES
# ==================================================

anomaly_query = """
SELECT
    meter_id,
    timestamp,
    ROUND(power_kw, 2) AS power_kw,
    ROUND(power_factor, 3) AS power_factor
FROM meter_readings
WHERE power_kw > 110
ORDER BY timestamp;
"""

anomaly_data = pd.read_sql_query(
    anomaly_query,
    conn
)

anomaly_data.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "anomalies.csv"
    ),
    index=False
)


conn.close()

print("=" * 50)
print("POWER BI DATA EXPORT")
print("=" * 50)

print("\nFiles generated:")

for file in os.listdir(OUTPUT_DIR):
    if file.endswith(".csv"):
        print("✓", file)

print("\nDashboard data ready!")