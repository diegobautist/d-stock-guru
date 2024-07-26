import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import requests
from datetime import datetime

#------------ Functions ------------#

# Function to get location data from IP address
def get_location(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()
    location = data['loc'].split(',')
    return {
        'User': data['ip'],
        'Latitude': float(location[0]),
        'Longitude': float(location[1])
    }


# Function to get real-time stock data from Yahoo Finance
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d", interval="1m")
    return hist

# Function to get stock data
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1mo")  
    return hist['Close']

#----------- Page design -----------#
# Function to update the background color
def set_background_color(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        .title-logo-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .title-logo-container h1 {{
            margin: 0;
            font-family: 'Arial', sans-serif;
            font-size: 2.5em;
            color: white;
            text-shadow: 2px 2px 4px #000000;
        }}
        .title-logo-container img {{
            height: 50px; 
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

#------------ Main Page ------------#

# Get the current month and year
current_month_year = datetime.now().strftime("%B %Y")

# Title with logo
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f"<h1 style='color: white;'>The D Stock Guru Selection Picks for {current_month_year}</h1>", unsafe_allow_html=True)
with col2:
    st.image("static/images/logo.png", use_column_width=True)

# Header
st.write(
    "This dashboard provides insights into stock market trends and allows you to interact with various widgets to customize your view."
)
# Disclaimer
st.write(
    "Disclaimer:"
)

# Disclamair message
st.info("The information provided here is for informational purposes only and should not be construed as financial advice. I am not a financial advisor. Any investment decisions you make should be based on your own research and knowledge. Always consider consulting with a professional financial advisor before making any investment decisions.", icon="ℹ️")

# Color picker to select background color
color = st.color_picker("Pick a color to custom your Background", "#1d1160")

# Update the background color based on the selected color
set_background_color(color)

# Interactive Table 
st.header("Interactive Table")
symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
selected_symbol = st.selectbox("Select a stock symbol", symbols)
stock_data = get_stock_data(selected_symbol)
st.dataframe(stock_data)

# Line Chart
st.header("Stock Price Trends")
stock_select = st.multiselect("Select multiple stocks", symbols)

# Fetch data for selected stocks
if stock_select:
    chart_data = pd.DataFrame()
    for symbol in stock_select:
        chart_data[symbol] = get_stock_data(symbol)
    
    # Plot the line chart
    st.line_chart(chart_data)
else:
    st.write("Please select at least one stock symbol to display the chart.")

#--------- Map ---------#
st.header("User Locations")
# Get the user's IP address
def get_public_ip():
    response = requests.get("https://httpbin.org/ip")
    return response.json()['origin']

# Get the user's IP address
user_ip = get_public_ip()

# Get location data for the user's IP address
user_location = get_location(user_ip)

# Create a DataFrame
map_data = pd.DataFrame([user_location])

# Display the map
st.map(map_data[['Latitude', 'Longitude']].rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}))
#----------------------#

# Buy or Sell
st.subheader("If you would like to buy or sell a stock, please enter the stock symbol and the number of shares you would like to trade.")

transaction_stock = st.selectbox("Select one of the stock options", symbols)

# Checkbox Widget
if st.checkbox('Show selected stock data'):
    st.bar_chart(get_stock_data(transaction_stock))

col1, col2 = st.columns([3, 1])
with col1:
    st.date_input("Select the date that you want the transaction to be made")
with col2:
    st.time_input("Select a time")

st.number_input("Enter total amount of Share", min_value=0, max_value=100, value=50)



st.radio("Choose an option", ['Buy', 'Sell'])

# Complete Widget
if st.button('Complete Trade'):
    st.success('Trade completed!', icon="✅")