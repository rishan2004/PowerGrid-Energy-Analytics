import pandas as pd
import numpy as np

np.random.seed(42)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

START_DATE = "2025-01-01"
DAYS = 90
INTERVAL_MINUTES = 15
NUM_METERS = 10

timestamps = pd.date_range(
    start=START_DATE,
    periods=DAYS * 24 * 60 // INTERVAL_MINUTES,
    freq=f"{INTERVAL_MINUTES}min"
)

# --------------------------------------------------
# Generate base data
# --------------------------------------------------

data = []

for meter in range(1, NUM_METERS + 1):

    for timestamp in timestamps:

        hour = timestamp.hour

        # Base load pattern
        if 0 <= hour < 6:
            base_load = 20
        elif 6 <= hour < 10:
            base_load = 45
        elif 10 <= hour < 17:
            base_load = 55
        elif 17 <= hour < 22:
            base_load = 75
        else:
            base_load = 40

        # Random variation
        power_kw = base_load + np.random.normal(0, 5)

        # Meter-specific variation
        power_kw *= np.random.uniform(0.85, 1.15)

        # Voltage
        voltage = np.random.normal(415, 5)

        # Power factor
        power_factor = np.clip(
            np.random.normal(0.92, 0.03),
            0.75,
            0.99
        )

        # Calculate approximate current
        current = (
            power_kw * 1000
            / (np.sqrt(3) * voltage * power_factor)
        )

        # 15-minute energy
        energy_kwh = power_kw * (INTERVAL_MINUTES / 60)

        # Temperature
        temperature = np.random.normal(28, 4)

        data.append([
            timestamp,
            f"M{meter:02d}",
            voltage,
            current,
            power_factor,
            power_kw,
            energy_kwh,
            temperature
        ])

# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------

columns = [
    "timestamp",
    "meter_id",
    "voltage",
    "current",
    "power_factor",
    "power_kw",
    "energy_kwh",
    "temperature"
]

df = pd.DataFrame(data, columns=columns)

# --------------------------------------------------
# Add abnormal consumption events
# --------------------------------------------------

anomaly_indices = np.random.choice(
    len(df),
    size=500,
    replace=False
)

# Increase power during abnormal events
df.loc[anomaly_indices, "power_kw"] *= np.random.uniform(
    1.5,
    2.2,
    size=len(anomaly_indices)
)

# Recalculate current so the electrical relationship remains valid
df["current"] = (
    df["power_kw"] * 1000
    / (
        np.sqrt(3)
        * df["voltage"]
        * df["power_factor"]
    )
)

# Recalculate energy
df["energy_kwh"] = (
    df["power_kw"]
    * (INTERVAL_MINUTES / 60)
)
# --------------------------------------------------
# Save
# --------------------------------------------------

output_path = "data/electricity_data.csv"

df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {output_path}")

print("\nFirst 5 rows:")
print(df.head())