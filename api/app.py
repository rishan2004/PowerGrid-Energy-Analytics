from flask import Flask, jsonify
import sqlite3
import pandas as pd
import os

app = Flask(__name__)

# --------------------------------------------------
# Database path
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(
    BASE_DIR,
    "data",
    "powergrid.db"
)


# --------------------------------------------------
# Database connection
# --------------------------------------------------

def get_connection():
    return sqlite3.connect(DB_PATH)


# --------------------------------------------------
# Home
# --------------------------------------------------

@app.route("/")
def home():

    return jsonify({
        "project": "PowerGrid Energy Analytics",
        "status": "API running",
        "version": "1.0"
    })


# --------------------------------------------------
# Summary
# --------------------------------------------------

@app.route("/api/summary")
def summary():

    conn = get_connection()

    query = """
    SELECT
        ROUND(SUM(energy_kwh), 2) AS total_energy_kwh,
        ROUND(AVG(power_kw), 2) AS average_power_kw,
        ROUND(MAX(power_kw), 2) AS peak_demand_kw,
        ROUND(AVG(power_factor), 3) AS average_power_factor
    FROM meter_readings;
    """

    result = pd.read_sql_query(query, conn)

    conn.close()

    return jsonify(
        result.to_dict(orient="records")[0]
    )


# --------------------------------------------------
# Meter Analysis
# --------------------------------------------------

@app.route("/api/meters")
def meters():

    conn = get_connection()

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

    conn.close()

    return jsonify(
        result.to_dict(orient="records")
    )


# --------------------------------------------------
# Hourly Load
# --------------------------------------------------

@app.route("/api/hourly-load")
def hourly_load():

    conn = get_connection()

    query = """
    SELECT
        CAST(strftime('%H', timestamp) AS INTEGER) AS hour,
        ROUND(AVG(power_kw), 2) AS average_load_kw
    FROM meter_readings
    GROUP BY hour
    ORDER BY hour;
    """

    result = pd.read_sql_query(query, conn)

    conn.close()

    return jsonify(
        result.to_dict(orient="records")
    )


# --------------------------------------------------
# Anomalies
# --------------------------------------------------

@app.route("/api/anomalies")
def anomalies():

    conn = get_connection()

    query = """
    SELECT
        meter_id,
        timestamp,
        ROUND(power_kw, 2) AS power_kw,
        ROUND(power_factor, 3) AS power_factor
    FROM meter_readings
    WHERE power_kw > 110
    ORDER BY power_kw DESC
    LIMIT 100;
    """

    result = pd.read_sql_query(query, conn)

    conn.close()

    return jsonify(
        result.to_dict(orient="records")
    )


# --------------------------------------------------
# Electrical Analysis
# --------------------------------------------------

@app.route("/api/electrical")
def electrical():

    conn = get_connection()

    query = """
    SELECT
        ROUND(AVG(voltage), 2) AS average_voltage,
        ROUND(AVG(current), 2) AS average_current,
        ROUND(AVG(power_factor), 3) AS average_power_factor,
        ROUND(AVG(power_kw), 2) AS average_real_power,
        ROUND(AVG(power_kw / power_factor), 2) AS average_apparent_power
    FROM meter_readings;
    """

    result = pd.read_sql_query(query, conn)

    conn.close()

    return jsonify(
        result.to_dict(orient="records")[0]
    )


# --------------------------------------------------
# Run Application
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("POWERGRID ENERGY ANALYTICS API")
    print("=" * 50)

    print(f"Database: {DB_PATH}")

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )