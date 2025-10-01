import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌍 Air Quality Index (AQI) Demo")
st.write("Upload a CSV with date/time and PM2.5 columns.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file is not None:
    # Try reading CSV
    try:
        df = pd.read_csv(uploaded_file)
    except UnicodeDecodeError:
        df = pd.read_csv(uploaded_file, encoding="latin1")

    st.subheader("📂 Dataset preview")
    st.dataframe(df.head())

    # Detect datetime column
    datetime_col = None
    for col in df.columns:
        if "date" in col.lower() or "time" in col.lower():
            datetime_col = col
            break

    # Handle separate year/month/day/hour columns
    if not datetime_col and set(['year','month','day','hour']).issubset(df.columns):
        df['datetime'] = pd.to_datetime(df[['year','month','day','hour']])
        datetime_col = 'datetime'

    if datetime_col and 'PM2.5' in df.columns:
        # Convert to datetime
        df[datetime_col] = pd.to_datetime(df[datetime_col], errors='coerce')
        df = df.dropna(subset=[datetime_col])
        df = df.sort_values(datetime_col)

        # Plot actual PM2.5
        st.subheader("📈 AQI Over Time")
        st.line_chart(df.set_index(datetime_col)['PM2.5'])

        # Simple forecast (moving average)
        df['forecast'] = df['PM2.5'].rolling(window=3).mean()
        st.subheader("📊 Forecast (last 10 values)")
        st.write(df[[datetime_col,'forecast']].tail(10))

        # Plot actual vs forecast
        fig, ax = plt.subplots()
        ax.plot(df[datetime_col], df['PM2.5'], label="Actual AQI")
        ax.plot(df[datetime_col], df['forecast'], label="Forecast (Moving Avg)")
        ax.legend()
        st.pyplot(fig)
    else:
        st.error("❌ Dataset must have a date/time column and a 'PM2.5' column.")