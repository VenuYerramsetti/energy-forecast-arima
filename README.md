# Energy Consumption Forecasting with ARIMA

## Project Overview
This project focuses on forecasting monthly energy consumption using seasonal ARIMA models with automated parameter tuning.

---

## Features

- Data preprocessing and visualization  
- Auto ARIMA model selection with pmdarima  
- Forecast generation with confidence intervals  
- Historical and forecast plot visualizations  
- Exporting results for Power BI integration  
- Designed for Azure cloud automation and smooth Git integration  

Additionally, the repository includes other data science projects like stock price forecasting, customer complaint NLP classification, university admission prediction, and data pipeline automation — demonstrating a wide range of machine learning and data engineering skills.

---

## Contents
- Data loading and preprocessing  
- Time series visualization  
- Seasonal ARIMA modeling and forecasting  
- Forecast result export  
- Visualization saving  
- Folder management for outputs  

---

## Folder Structure

All output files (CSVs + PNG plots) are saved in:

C:\Users\venum\energy-forecast-arima\


with these files:

- `energy_original.csv` — Historical data
- `energy_forecast.csv` — Forecasted values + confidence intervals
- `energy_combined.csv` — Historical + forecast combined (Power BI/Azure ready)
- `energy_original_plot.png` — Plot of historical data
- `energy_forecast_plot.png` — Plot of forecast + confidence intervals

---

## Setup Instructions

### Requirements
- Python 3.8+  
- pandas  
- matplotlib  
- pmdarima  

Use `pip install -r requirements.txt` to install dependencies.

---

## Usage
Run the main notebook or script to generate forecasts and visualizations. Outputs are saved in timestamped folders under the `output` directory to avoid overwriting previous runs.

python energy_forecast_arima.py


Notes
The script overwrites output files on each run — avoiding duplicate or accumulating data.

The folder and files are structured for easy integration with Git, Power BI, and Azure.

Plots are saved as PNG files and displayed during runtime for quick visualization.


---

## Contribution
Feel free to fork, submit issues, or create pull requests.

---

## License
MIT License