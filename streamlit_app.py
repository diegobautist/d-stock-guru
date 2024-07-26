import streamlit as st
import pandas as pd
import numpy as np

# Custom CSS to change backgroup color
st.markdown(
    """
    <style>
    .stApp {
        background-color: purple;
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
        height: 50px; /* Adjust the height as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with logo
st.markdown(
    """
    <div class="title-logo-container">
        <h1>The D Stock Guru!</h1>
        <img src="images/logo.png" alt="Logo">
    </div>
    """,
    unsafe_allow_html=True
)

# Header
st.write(
    "Welcome to the D Stock Guru! This app will help you analyze the stock market and make informed decisions."
)

# Interactive Table
st.header("Interactive Table")
data = {
    'Stock': ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'],
    'Price': [150, 2800, 300, 3500, 700],
    'Change': [1.2, -0.5, 0.8, 1.5, -2.3]
}
df = pd.DataFrame(data)
st.dataframe(df)

# Line Chart
st.header("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['AAPL', 'GOOGL', 'MSFT']
)
st.line_chart(chart_data)

# Area Chart
st.header("Area Chart")
st.area_chart(chart_data)

# Map
st.header("Map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# Button Widget
if st.button('Click me'):
    st.write('Button clicked!')

# Checkbox Widget
if st.checkbox('Show dataframe'):
    st.write(df)

# Feedback Boxes
st.success('Success message')
st.info('Information message')
st.warning('Warning message')
st.error('Error message')
try:
    raise ValueError("An exception occurred")
except ValueError as e:
    st.exception(e)

# Additional Widgets
st.header("Additional Widgets")
st.radio("Choose an option", ['Option 1', 'Option 2', 'Option 3'])
st.selectbox("Select a stock", ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'])
st.multiselect("Select multiple stocks", ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'])
st.slider("Select a range", 0, 100, (25, 75))
st.select_slider("Select a value", options=['Low', 'Medium', 'High'])
st.text_input("Enter text")
st.number_input("Enter a number", min_value=0, max_value=100, value=50)
st.date_input("Select a date")
st.time_input("Select a time")
st.file_uploader("Upload a file")
st.color_picker("Pick a color")

# Run the app with: streamlit run streamlit_app.py