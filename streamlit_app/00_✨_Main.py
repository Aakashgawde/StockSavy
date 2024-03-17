import streamlit as st

st.set_page_config(
    page_title="Stock Prediction App",
    page_icon="✨",
)

st.markdown(
    """# 📈 **StockSavy**
### **Predicting Stocks with ML**

**StockSavy is an ML-powered stock price prediction app built with Python and Streamlit. It utilizes machine learning models to predict stock prices and help investors make data-driven decisions.**

## 🏗️ **How It's Built**

StockSavy is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **YFinance** - To fetch financial data from Yahoo Finance API
- **StatsModels** - To build the LSTM time series prediction model
- **Plotly** - To create interactive financial charts

The app workflow is:

1. User selects a stock ticker
2. Historical data is fetched with YFinance
3. LSTM model is trained on the data 
4. Model makes multi-day price forecasts
5. Results are plotted with Plotly

## 🎯 **Key Features**

- **Real-time data** - Fetch latest prices and fundamentals 
- **Financial charts** - Interactive historical and forecast charts
- **LSTM prediction** - Make statistically robust predictions
- **Backtesting** - Evaluate model performance
- **Responsive design** - Works on all devices



## 📈 **Future Roadmap**

Some potential features for future releases:

- **More advanced prediction models like ARIMA**
- **Quantitative trading strategies**
- **Portfolio optimization and tracking**
- **Additional fundamental data**
- **User account system**

## **⚖️ Disclaimer**
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**
"""
)
