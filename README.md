
```markdown
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Last Commit](https://img.shields.io/github/last-commit/VenuYerramsetti/energy-forecast-arima)
![Repo Size](https://img.shields.io/github/repo-size/VenuYerramsetti/energy-forecast-arima)

![Dashboard Preview](dashboard_preview.png)

# ⚡ Energy Consumption Forecasting with ARIMA + Power BI + Azure

Predict monthly energy consumption using advanced time series modeling, visualized beautifully in **Power BI**, and ready for **Azure** automation.

---

## 📌 Overview

This project forecasts monthly energy usage using **Seasonal ARIMA (SARIMA)** models with automated hyperparameter tuning via `pmdarima`. The results are exported, visualized in Power BI, and structured to enable easy deployment to Azure for end-to-end automation.

---

## 🚀 Features

- ✅ **Time Series Forecasting** with Seasonal ARIMA
- 📈 Historical vs Forecast plots
- 📊 Power BI dashboard with:
  - Line chart (Historical + Forecast)
  - Table of forecast with confidence intervals
  - Interactive date slicer
  - Source card (data attribution)
- 💾 Auto-export of forecast results to CSV
- ☁️ Azure-ready structure
- 🔄 Seamless Git integration

---

## 🧠 Technologies Used

| Area          | Tool               |
| ------------- | ------------------ |
| Forecasting   | Python, pmdarima   |
| Data Wrangling| pandas             |
| Visualization | matplotlib, Power BI |
| Deployment    | Azure-compatible output |
| Version Control | Git + GitHub     |

---

## 📂 File Outputs

After running the script, these files are generated:

```

energy\_forecast.csv           # Combined forecast + historical data
forecast\_only.csv             # Forecasted values only
original\_energy\_data.csv      # Original dataset
energy\_forecast\_plot.png      # Forecast plot with confidence intervals
original\_energy\_consumption.png  # Historical consumption plot
energy\_forecast.pbix          # Power BI Dashboard file

````

---

## 📊 Power BI Dashboard Features

- 🔷 Line Chart: Historical and forecast consumption
- 📅 Date Slicer: Filter data by date (dropdown or range)
- 📋 Table: Forecast values + Lower/Upper confidence intervals
- 🧾 Source Note: Attribution to Python preprocessing

---

## 🛠️ Setup Instructions

### Requirements

Ensure Python 3.8+ is installed, then install dependencies:

```bash
pip install -r requirements.txt
````

### Run the Forecast Script

```bash
python energy_forecast_arima.py
```

---

## ☁️ Azure Integration

* Outputs structured for Azure Blob Storage upload
* Can be automated via Azure Functions or Logic Apps
* Future plans: Connect Power BI directly to Azure Blob with refresh

---

## ☁️ Azure Machine Learning Deployment

Tested on Azure ML:

* Workspace: `energy-ml-ws`
* Compute Instance: `arima-instance`
* Environment: `arima-env` (Python 3.10 + pmdarima)
* Script: `run_forecast_job.py`

---

## 📁 Getting Output Plots and Logs

* Forecast plots (`energy_forecast_plot.png`) are saved in the `job_logs` directory.
* You can view/download them from Azure ML compute instance via Jupyter or terminal.
* Alternatively, take screenshots from the Azure ML job logs or Power BI dashboard.

---

## 💡 Notes

* The script overwrites output files on each run to avoid clutter.
* Power BI dashboard reads data directly from `energy_forecast.csv`.
* Use Git for version control and Azure for automation.

---

## 🤝 Contribution

Pull requests and ideas welcome! If this project helps you, please ⭐ star the repo.

---

## 🪪 License

MIT License

---

## 🧾 Git Commands to Commit & Push

Make sure you’re in the project root (`energy-forecast-arima/`) and all new files are ready.

```bash
# Optional: Clean old tracked files that should be ignored
git rm -r --cached output/

# Pull latest changes
git pull origin main

# Add all files
git add .

# Commit with a clear message
git commit -m "🔄 Updated forecasting script, Power BI dashboard, and outputs"

# Push to GitHub
git push origin main
```


