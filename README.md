# ⚡ PowerGrid Energy Analytics & Electrical Operations Dashboard

An end-to-end electrical energy analytics project combining **Python, SQL, MATLAB and Power BI** to analyze energy consumption, electrical operating parameters, peak demand and abnormal power events across multiple meters.

---

## 📊 Project Overview

This project analyzes **86,400 electrical measurements across 10 meters** and converts raw electrical measurements into actionable energy and grid-operation insights.

The project combines:

- Python-based data generation and analytics
- SQL-based energy and meter analysis
- MATLAB-based electrical engineering calculations
- Power BI-based interactive visualization
- Anomaly detection for high-power events

### Key Results

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

# 🏗️ Project Architecture

```text
Raw Electrical Data
        │
        ▼
     Python
  Data Generation
  Data Analysis
        │
        ├───────────────┐
        ▼               ▼
      SQL            MATLAB
   Analytics       Electrical
   & Queries       Calculations
        │               │
        └───────┬───────┘
                ▼
            Power BI
        Interactive Dashboard
                │
                ▼
      Grid & Operational Insights
