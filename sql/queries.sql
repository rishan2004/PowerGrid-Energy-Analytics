-- ==========================================
-- POWERGRID ENERGY ANALYTICS
-- SQL ANALYSIS
-- ==========================================


-- 1. Total energy consumption

SELECT
    ROUND(SUM(energy_kwh), 2) AS total_energy_kwh
FROM meter_readings;


-- 2. Average power and peak demand

SELECT
    ROUND(AVG(power_kw), 2) AS average_power_kw,
    ROUND(MAX(power_kw), 2) AS peak_demand_kw
FROM meter_readings;


-- 3. Average power factor

SELECT
    ROUND(AVG(power_factor), 3) AS average_power_factor
FROM meter_readings;


-- 4. Energy consumption by meter

SELECT
    meter_id,
    ROUND(SUM(energy_kwh), 2) AS total_energy_kwh
FROM meter_readings
GROUP BY meter_id
ORDER BY total_energy_kwh DESC;


-- 5. Average load by hour

SELECT
    CAST(strftime('%H', timestamp) AS INTEGER) AS hour,
    ROUND(AVG(power_kw), 2) AS average_load_kw
FROM meter_readings
GROUP BY hour
ORDER BY hour;


-- 6. Peak demand by meter

SELECT
    meter_id,
    ROUND(MAX(power_kw), 2) AS peak_demand_kw
FROM meter_readings
GROUP BY meter_id
ORDER BY peak_demand_kw DESC;


-- 7. Low power-factor readings

SELECT
    meter_id,
    timestamp,
    power_factor
FROM meter_readings
WHERE power_factor < 0.85
ORDER BY power_factor ASC;


-- 8. High consumption events

SELECT
    meter_id,
    timestamp,
    power_kw,
    energy_kwh
FROM meter_readings
WHERE power_kw > 110
ORDER BY power_kw DESC;