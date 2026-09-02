
# ⚡ PowerGrid Energy Analytics & Electrical Operations Dashboard

An end-to-end electrical energy analytics project combining **Python, SQL, MATLAB and Power BI** to analyze energy consumption, electrical operating parameters, peak demand, meter performance and abnormal power events.

---

## 📌 Project Overview

This project analyzes **86,400 electrical measurements across 10 meters** and transforms raw electrical measurements into useful energy and grid-operation insights.

The project combines electrical engineering analysis with data analytics and business intelligence.

### Project Components

- 🐍 **Python** — Data generation, preprocessing, statistical analysis and anomaly detection
- 🗄️ **SQL / SQLite** — Energy, meter and peak-demand analytics
- ⚡ **MATLAB** — Electrical power calculations and validation
- 📊 **Power BI** — Interactive dashboard and visualization
- 🌐 **Python API** — Project data access through an API
- 🔧 **Git & GitHub** — Version control and project documentation

---

## 📊 Key Results

| Metric | Result |
|---|---:|
| Electrical Measurements | 86,400 |
| Monitored Meters | 10 |
| Total Energy | 1,030,988.61 kWh |
| Average Power | 47.73 kW |
| Peak Demand | 202.69 kW |
| Average Power Factor | 0.920 |
| Load Factor | 0.235 |
| Detected Anomalies | 157 |

---

## 🏗️ Project Architecture

```text
                 ELECTRICAL MEASUREMENT DATA
                           │
                           ▼
                    ┌─────────────┐
                    │   PYTHON    │
                    │             │
                    │ Data        │
                    │ Generation  │
                    │ Analysis    │
                    │ Anomalies   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   SQLite    │
                    │  Database   │
                    └──────┬──────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
          ┌─────────────┐     ┌─────────────┐
          │     SQL     │     │   MATLAB    │
          │  Analytics  │     │ Electrical  │
          │             │     │ Calculations│
          └──────┬──────┘     └──────┬──────┘
                 │                   │
                 └─────────┬─────────┘
                           ▼
                    ┌─────────────┐
                    │  POWER BI   │
                    │  Dashboard  │
                    └──────┬──────┘
                           │
                           ▼
                 GRID & OPERATIONAL
                       INSIGHTS
---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data generation, processing, analytics and anomaly detection |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical calculations |
| SQL | Energy and meter-level analytics |
| SQLite | Local analytical database |
| MATLAB | Electrical calculations and validation |
| Power BI | Interactive dashboard and visualization |
| DAX | Power BI measures and calculations |
| Git | Version control |
| GitHub | Project hosting and documentation |

---

# 🚀 How to Run

## Python

Create a virtual environment:

```bash
python -m venv venv
Activate it on Windows:
venv\Scripts\activate

Install the required packages:
pip install pandas numpy
Run the main analysis:
python python/analysis.py
Run SQL analytics:
python python/sql_analysis.py

MATLAB

Open the following file in MATLAB:matlab/electrical_analysis.m
Run the script to perform the electrical calculations and generate the analysis results.

Power BI

Open:dashboard/PowerGrid_Energy_Analytics_Dashboard.pbix
The dashboard provides interactive exploration of the electrical and energy analytics.

The electrical dataset used in this project is a synthetically generated dataset designed for analytical and educational purposes.

The dataset was constructed with relationships between voltage, current, power factor and electrical power so that the resulting calculations could be validated using electrical engineering equations.

It does not represent confidential operational data from an actual utility, substation or power-grid operator.

.

🎯 Project Objective

The objective of this project is to demonstrate how electrical engineering principles and data analytics can be combined to analyze electrical operating conditions, identify abnormal power events and present actionable insights through an interactive business-intelligence dashboard.
