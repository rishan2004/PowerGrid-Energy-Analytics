%% POWERGRID ELECTRICAL ANALYSIS
% Electrical Engineering Analysis
% PowerGrid Energy Analytics Project

clear;
clc;
close all;

%% POWERGRID ELECTRICAL ANALYSIS

clear;
clc;
close all;

%% Locate project files

scriptFolder = fileparts(mfilename('fullpath'));

projectFolder = fileparts(scriptFolder);

dataPath = fullfile(projectFolder, 'data', 'electricity_data.csv');

fprintf('Looking for dataset at:\n%s\n\n', dataPath);

if ~isfile(dataPath)
    error('Dataset not found at: %s', dataPath);
end

data = readtable(dataPath);

data.timestamp = datetime(data.timestamp);

fprintf('Dataset loaded successfully!\n');
fprintf('Rows: %d\n', height(data));
fprintf('Columns: %d\n\n', width(data));

fprintf('============================================\n');
fprintf('POWERGRID ELECTRICAL ANALYSIS\n');
fprintf('============================================\n');

%% ------------------------------------------------
% Basic Electrical Parameters
% -------------------------------------------------

V = data.voltage;
I = data.current;
P = data.power_kw;
PF = data.power_factor;

%% ------------------------------------------------
% Apparent Power
% S = P / PF
% -------------------------------------------------

S = P ./ PF;

%% ------------------------------------------------
% Reactive Power
% Q = P * tan(acos(PF))
% -------------------------------------------------

Q = P .* tan(acos(PF));

%% ------------------------------------------------
% Three Phase Power Verification
% P = sqrt(3) * V * I * PF
% -------------------------------------------------

P_calculated = sqrt(3) .* V .* I .* PF / 1000;

%% ------------------------------------------------
% Current Error
% -------------------------------------------------

power_error = abs(P - P_calculated);

fprintf('\n--- ELECTRICAL CALCULATIONS ---\n');

fprintf('Average Voltage: %.2f V\n', mean(V));
fprintf('Average Current: %.2f A\n', mean(I));
fprintf('Average Power Factor: %.3f\n', mean(PF));
fprintf('Average Real Power: %.2f kW\n', mean(P));
fprintf('Average Apparent Power: %.2f kVA\n', mean(S));
fprintf('Average Reactive Power: %.2f kVAR\n', mean(Q));

fprintf('\nMaximum Current: %.2f A\n', max(I));
fprintf('Maximum Real Power: %.2f kW\n', max(P));

fprintf('\nMaximum calculation error: %.6f kW\n', ...
    max(power_error));

%% ------------------------------------------------
% Load Factor
% -------------------------------------------------

average_load = mean(P);
peak_load = max(P);

load_factor = average_load / peak_load;

fprintf('\n--- LOAD ANALYSIS ---\n');

fprintf('Average Load: %.2f kW\n', average_load);
fprintf('Peak Load: %.2f kW\n', peak_load);
fprintf('Load Factor: %.3f\n', load_factor);

%% ------------------------------------------------
% Hourly Load Profile
% -------------------------------------------------

data.hour = hour(data.timestamp);
hourly_load = groupsummary(data, 'hour', 'mean', 'power_kw');
figure;
plot(hourly_load.hour, hourly_load.mean_power_kw, 'LineWidth', 1.5);

xlabel('Hour of Day');
ylabel('Average Power (kW)');
title('24-Hour Electricity Load Profile');

grid on;

%% ------------------------------------------------
% Power Factor Trend
% -------------------------------------------------
hourly_pf = groupsummary(data, 'hour', 'mean', 'power_factor');

figure;

plot(hourly_pf.hour,hourly_pf.mean_power_factor,'LineWidth', 1.5);

xlabel('Hour of Day');
ylabel('Average Power Factor');
title('Hourly Power Factor Profile');

grid on;

%% ------------------------------------------------
% Reactive Power Profile
% -------------------------------------------------

data.reactive_power_kvar = Q;

hourly_q = groupsummary(data, 'hour', 'mean', 'reactive_power_kvar');
figure;

plot(hourly_q.hour,hourly_q.mean_reactive_power_kvar,'LineWidth', 1.5);

xlabel('Hour of Day');
ylabel('Reactive Power (kVAR)');
title('Hourly Reactive Power Profile');

grid on;

%% ------------------------------------------------
% Current Profile
% -------------------------------------------------

hourly_current = groupsummary(data, 'hour', 'mean', 'current');

figure;

plot(hourly_current.hour,hourly_current.mean_current,'LineWidth', 1.5);

xlabel('Hour of Day');
ylabel('Current (A)');
title('Hourly Current Profile');

grid on;

%% ------------------------------------------------
% Export Electrical Results
% -------------------------------------------------

electrical_results = table( ...
    data.timestamp, ...
    data.meter_id, ...
    V, ...
    I, ...
    P, ...
    PF, ...
    S, ...
    Q, ...
    P_calculated, ...
    power_error, ...
    'VariableNames', { ...
        'timestamp', ...
        'meter_id', ...
        'voltage_V', ...
        'current_A', ...
        'real_power_kW', ...
        'power_factor', ...
        'apparent_power_kVA', ...
        'reactive_power_kVAR', ...
        'calculated_power_kW', ...
        'power_error_kW' ...
    });

outputPath = fullfile(scriptFolder, '..', 'data', 'electrical_results.csv');

writetable(electrical_results, outputPath);
fprintf('\nElectrical results exported successfully.\n');
fprintf('\nMATLAB ANALYSIS COMPLETED.\n');