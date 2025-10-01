# AirQualityIndx
This project is a Streamlit-based web application for analyzing and forecasting Air Quality Index (AQI) values. It allows users to upload their own air quality datasets (CSV format) and instantly visualize AQI levels over time. The app also applies a simple moving average model to generate forecasts, helping users understand pollution trends. 
## 📌 Project Overview
This is a **Streamlit-based web application** for analyzing and forecasting **Air Quality Index (AQI)** values.  
It allows users to upload their own air quality datasets in CSV format and instantly visualize AQI trends over time.  
The app also provides a simple **moving average forecast** to help understand air pollution patterns.

---

## 🚀 Features
- 📂 Upload CSV dataset
- 📊 Auto-detects **date/time column**
- 🌫️ Supports AQI values (e.g., `PM2.5`)
- 📈 Interactive time-series line chart
- 🔮 Forecast using **simple moving average**
- 🖥️ Clean and user-friendly UI with **Streamlit**

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Streamlit** → Web App Framework
- **Pandas** → Data Handling
- **Matplotlib** → Visualization

---

## 📂 Dataset Format
The dataset must contain:
- A **date/time column** (example: `datetime`, `date`, or separate `year,month,day,hour`)
- An **AQI column** (example: `PM2.5`)

### ✅ Example Dataset
```csv
datetime,PM2.5
2025-09-30 01:00:00,82
2025-09-30 02:00:00,79
2025-09-30 03:00:00,85

