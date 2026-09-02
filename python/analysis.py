import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/electricity_data.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

print("=" * 50)
print("POWERGRID ENERGY ANALYTICS")
print("=" * 50)

# --------------------------------------------------
# 1. DATA QUALITY
# --------------------------------------------------

print("\n--- DATA QUALITY ---")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing values:")
print(df.isnull().sum())

# --------------------------------------------------
# 2. BASIC ENERGY STATISTICS
# --------------------------------------------------

total_energy = df["energy_kwh"].sum()
average_power = df["power_kw"].mean()
peak_demand = df["power_kw"].max()
average_pf = df["power_factor"].mean()

print("\n--- ENERGY STATISTICS ---")

print(f"Total Energy:       {total_energy:,.2f} kWh")
print(f"Average Power:      {average_power:,.2f} kW")
print(f"Peak Demand:        {peak_demand:,.2f} kW")
print(f"Average Power Factor: {average_pf:.3f}")

# --------------------------------------------------
# 3. LOAD FACTOR
# --------------------------------------------------

load_factor = average_power / peak_demand

print(f"Load Factor:        {load_factor:.3f}")

# --------------------------------------------------
# 4. PEAK HOUR
# --------------------------------------------------

df["hour"] = df["timestamp"].dt.hour

hourly_load = (
    df.groupby("hour")["power_kw"]
    .mean()
    .sort_values(ascending=False)
)

peak_hour = hourly_load.index[0]

print("\n--- PEAK ANALYSIS ---")

print(f"Peak Average Hour: {peak_hour}:00")
print("\nHourly Average Load:")
print(hourly_load)

# --------------------------------------------------
# 5. METER ANALYSIS
# --------------------------------------------------

meter_summary = (
    df.groupby("meter_id")
    .agg(
        total_energy_kwh=("energy_kwh", "sum"),
        average_power_kw=("power_kw", "mean"),
        peak_power_kw=("power_kw", "max"),
        average_power_factor=("power_factor", "mean")
    )
    .sort_values(
        "total_energy_kwh",
        ascending=False
    )
)

print("\n--- METER PERFORMANCE ---")
print(meter_summary)

# --------------------------------------------------
# 6. ANOMALY DETECTION
# --------------------------------------------------

mean_power = df["power_kw"].mean()
std_power = df["power_kw"].std()

threshold = mean_power + (3 * std_power)

df["anomaly"] = df["power_kw"] > threshold

anomalies = df[df["anomaly"]]

print("\n--- ANOMALY ANALYSIS ---")

print(f"Anomaly Threshold: {threshold:.2f} kW")
print(f"Anomalies Detected: {len(anomalies)}")

# --------------------------------------------------
# 7. SAVE ANALYTICS OUTPUT
# --------------------------------------------------

meter_summary.to_csv(
    "data/meter_summary.csv"
)

hourly_load.to_csv(
    "data/hourly_load.csv"
)

anomalies.to_csv(
    "data/anomalies.csv",
    index=False
)

print("\nAnalytics files generated successfully!")

print("\nProject analysis completed.")