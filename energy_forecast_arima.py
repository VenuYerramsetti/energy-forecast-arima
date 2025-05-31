#!/usr/bin/env python
# coding: utf-8

# Energy Consumption Forecasting with ARIMA

# 📦 Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from pmdarima import auto_arima
import warnings
import os

warnings.filterwarnings("ignore")

# 📁 Ensure outputs directory exists
os.makedirs('outputs', exist_ok=True)

# 📊 Step 2: Load Sample Energy Dataset (monthly data)
url = 'https://raw.githubusercontent.com/selva86/datasets/master/a10.csv'
df = pd.read_csv(url)

# Rename columns and prepare datetime index
df.columns = ['Date', 'Energy_Consumption']
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 🖼 Step 3: Visualize Original Time Series
plt.figure(figsize=(10, 5))
plt.plot(df['Energy_Consumption'], label='Energy Usage')
plt.title("Monthly Energy Consumption")
plt.xlabel("Date")
plt.ylabel("Consumption")
plt.grid(True)
plt.legend()
plt.savefig("outputs/original_energy_consumption.png")  # Save plot as PNG
plt.show()

# Save original historical data to CSV
df.to_csv("outputs/original_energy_data.csv")

# 🧠 Step 4: Auto ARIMA Model Fitting
model = auto_arima(df['Energy_Consumption'], 
                   seasonal=True, m=12, 
                   trace=True, 
                   suppress_warnings=True,
                   stepwise=True)

# Save model summary to text file
with open("outputs/arima_model_summary.txt", "w") as f:
    f.write(str(model.summary()))

# 📈 Step 5: Forecast Future Values
n_periods = 12  # Forecast next 12 months
forecast, conf_int = model.predict(n_periods=n_periods, return_conf_int=True)

# Generate future dates for forecast
last_date = df.index[-1]
future_dates = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=n_periods, freq='MS')

# Create Forecast DataFrame with confidence intervals
forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Forecast': forecast,
    'Lower_CI': conf_int[:, 0],
    'Upper_CI': conf_int[:, 1],
    'Energy_Consumption': [None]*n_periods
})
forecast_df.set_index('Date', inplace=True)

# Save forecast-only data to CSV
forecast_df[['Forecast', 'Lower_CI', 'Upper_CI']].to_csv("outputs/forecast_only.csv")

# 📊 Step 6: Plot Forecast along with Historical Data
plt.figure(figsize=(12, 6))
plt.plot(df['Energy_Consumption'], label='Historical')
plt.plot(forecast_df['Forecast'], label='Forecast', color='red')
plt.fill_between(forecast_df.index, forecast_df['Lower_CI'], forecast_df['Upper_CI'], color='pink', alpha=0.3)
plt.title("Energy Consumption Forecast (ARIMA)")
plt.xlabel("Date")
plt.ylabel("Consumption")
plt.legend()
plt.grid(True)
plt.savefig("outputs/energy_forecast_plot.png")  # Save forecast plot as PNG
plt.show()

# 📝 Step 7: Combine Historical + Forecast Data and Export to CSV
df_with_forecast_cols = df.copy()
df_with_forecast_cols['Forecast'] = None
df_with_forecast_cols['Lower_CI'] = None
df_with_forecast_cols['Upper_CI'] = None

combined_df = pd.concat([df_with_forecast_cols, forecast_df], axis=0)
combined_df = combined_df[['Energy_Consumption', 'Forecast', 'Lower_CI', 'Upper_CI']]
combined_df.to_csv("outputs/energy_forecast.csv")

# ✔️ Final log message
print("✅ Output files saved to the 'outputs/' directory:")
print(" - original_energy_data.csv")
print(" - forecast_only.csv")
print(" - energy_forecast.csv")
print(" - original_energy_consumption.png")
print(" - energy_forecast_plot.png")
print(" - arima_model_summary.txt")
