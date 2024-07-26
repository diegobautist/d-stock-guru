import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime

# Custom CSS for Design
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1d1160;
    }
    .title-logo-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .title-logo-container h1 {
        margin: 0;
        font-family: 'Arial', sans-serif;
        font-size: 2.5em;
        color: white;
        text-shadow: 2px 2px 4px #000000;
    }
    .title-logo-container img {
        height: 50px; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with logo
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("<h1 style='color: white;'>The D Stock Guru Market Dashboard</h1>", unsafe_allow_html=True)
with col2:
    st.image("static/images/logo.png", use_column_width=True)

# Header
st.write(
    "This dashboard provides insights into stock market trends and allows you to interact with various widgets to customize your view."
)

# Function to get real-time stock data from Yahoo Finance
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d", interval="1m")
    return hist

# Interactive Table 
st.header("Interactive Table")
symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
selected_symbol = st.selectbox("Select a stock symbol", symbols)
stock_data = get_stock_data(selected_symbol)
st.write(stock_data)

# Area Chart
st.header("Stock Price Trends")
st.area_chart(stock_data['Close'])

# Map (for demonstration purposes, using random data)
st.header("Company Locations")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# Button Widget
if st.button('Click me'):
    st.write('Button clicked!')

# Checkbox Widget
if st.checkbox('Show stock data'):
    st.write(stock_data)

# Feedback Boxes
st.success('Dashboard loaded successfully!')

# Additional Widgets
st.header("Additional Widgets")
st.radio("Choose an option", ['Option 1', 'Option 2', 'Option 3'])
st.multiselect("Select multiple stocks", symbols)
st.slider("Select a range", 0, 100, (25, 75))
st.select_slider("Select a value", options=['Low', 'Medium', 'High'])
st.text_input("Enter text")
st.number_input("Enter a number", min_value=0, max_value=100, value=50)
st.date_input("Select a date", value=datetime.date.today())
st.time_input("Select a time")
st.file_uploader("Upload a file")
st.color_picker("Pick a color")

# Run the app with: streamlit run streamlit_app.py