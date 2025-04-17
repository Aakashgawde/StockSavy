# 📈 Stock Price Prediction using LSTM

![LSTM Forecast](https://img.shields.io/badge/Machine%20Learning-LSTM-blue)
![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-orange)

## 🧠 Project Overview

This project aims to build a robust and accurate stock price prediction system using **Long Short-Term Memory (LSTM)** networks — a special type of Recurrent Neural Network (RNN) tailored for time series forecasting. The system helps investors and traders make informed decisions by analyzing historical stock data and predicting future price movements.


## 🎯 Objectives

- Accurately predict stock prices using LSTM neural networks.
- Provide investors with insights for better decision-making.
- Build a web-based interface using Streamlit for ease of use.
- Visualize historical and predicted stock data.
- Fetch and display live financial news related to the selected stock.

---

## 🔍 Key Features

- 📊 LSTM-based time series prediction
- 🌐 Web app developed with **Streamlit**
- 📰 Real-time news updates using financial APIs
- 📈 Dynamic visualization using **Matplotlib** and **Plotly**
- 📤 Input stock ticker, exchange, time period, and intervals
- 🧪 Robust testing & evaluation (MSE, RMSE, MAE)
- 📦 Scalable, modular design

---

## 📂 Modules

1. **Data Collection** - Fetch historical stock data using `yfinance` and APIs.
2. **Preprocessing** - Clean, normalize, and split the data.
3. **Feature Engineering** - Extract meaningful time series patterns.
4. **Model Building** - LSTM layers for sequence prediction.
5. **Model Evaluation** - Using MSE, RMSE, MAE.
6. **Web Interface** - Built with Streamlit for input & prediction.
7. **Visualization** - Graphs for actual vs. predicted prices.
8. **News Retrieval** - Display financial news for informed analysis.

---

## 🛠️ Tech Stack

- **Python** 3.x
- **Jupyter Notebook**
- **Streamlit**
- **VS Code**
- **LSTM (Keras/TensorFlow)**
- **Libraries**: NumPy, Pandas, Scikit-learn, Matplotlib, Plotly, yfinance, pandas_datareader

---

## 🧪 Testing Approach

- ✅ White-box testing on LSTM internal logic
- ✅ Black-box testing for UI & prediction outputs
- ✅ 16 test cases for data input, prediction accuracy, scalability & UI validation

---

## 📊 Model Performance

- Evaluation metrics:
  - **70% prediction accuracy**
  - MAPE-based comparison of predicted vs actual stock prices
- Accuracy validated across multiple trading dates using real stock data

