
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Simulated data (2015–2024)
years = np.arange(2015, 2025)
gdp_growth = np.array([2.1, 1.2, 2.2, 1.8, 1.7, 0.5, -2.4, 1.6, 2.3, 2.0])
consumer_spending = np.linspace(100, 140, 10)
search_trend = np.linspace(50, 120, 10)
sustainable_brands = np.linspace(10, 80, 10).astype(int)
revenue = 60 * (1 + (0.5 * gdp_growth/100 + 0.3 * (search_trend - 50)/100 + 0.2 * (consumer_spending - 100)/100))

df = pd.DataFrame({
    "Year": years,
    "GDP Growth (%)": gdp_growth,
    "Consumer Spending": consumer_spending,
    "Search Trend Index": search_trend,
    "Sustainable Brands": sustainable_brands,
    "Fashion Revenue ($B)": revenue.round(2)
})

# UI
st.title("Fashion Industry Growth Predictor")
st.write("A simplified model forecasting fashion revenue based on macro trends.")

# Inputs
gdp = st.slider("Projected GDP Growth (%)", -5.0, 5.0, 2.0, 0.1)
spend = st.slider("Consumer Spending Index", 100, 160, 135)
trend = st.slider("Search Trend Index", 50, 150, 120)
brands = st.slider("Number of Sustainable Brands", 10, 200, 85)

# Forecast
forecast = 60 * (1 + (0.5 * gdp/100 + 0.3 * (trend - 50)/100 + 0.2 * (spend - 100)/100))
st.metric("Forecasted Fashion Revenue", f"${forecast:.2f}B")

# Show historical chart
fig = px.line(df, x='Year', y='Fashion Revenue ($B)', title="Historical Fashion Revenue")
st.plotly_chart(fig)
