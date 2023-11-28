import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor
from sklearn import metrics
import plotly.express as px

# Load the dataset with a specific encoding
file_path = 'fuel.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')  # or encoding='latin1'

# Sidebar for navigation
page = st.sidebar.selectbox("Select a page", ["Home", "Visualization", "Predictions"])

# Main content based on selected page
if page == "Home":
    st.title("Fuel Price Analysis and Prediction")
    st.header("Welcome to the Fuel Price Prediction App!")
    st.write(
        "This app allows you to explore the historical trends of fuel prices in Zambia "
        "and provides predictions using various machine learning algorithms."
    )
    st.write(
    "This app allows you to explore the historical trends of fuel prices in Zambia "
    "and provides predictions using various machine learning algorithms. Navigate through "
    "different sections to visualize fuel prices over time, and evaluate the performance of "
    "different models in predicting petrol and diesel prices."
)

    st.subheader("Instructions:")
    st.write(
        "1. **Visualization Page:** Explore visualizations of fuel prices over time using interactive graphs."
        "\n2. **Predictions Page:** Evaluate the performance of different machine learning models for predicting "
        "petrol and diesel prices based on dollar and crude oil prices."
    )

    st.subheader("Getting Started:")
    st.write(
        "To begin, use the sidebar on the left to navigate between the Visualization Page and Predictions Page. "
        "Feel free to interact with the charts and evaluate the predictions made by different machine learning models."
    )

    st.subheader("About the Data:")
    st.write(
        "The data used in this app is sourced from the Energy regulation board, international crude prices, containing information about dates, "
        "dollar prices, crude oil prices, petrol prices, and diesel prices in Zambia. The app leverages various "
        "machine learning algorithms to make predictions based on historical data."
    )

    st.subheader("Ready to Explore?")
    st.write(
        "Click on the 'Visualization Page' and 'Predictions Page' in the sidebar to start exploring fuel prices in Zambia. "
        "Feel free to analyze the visualizations and evaluate the performance of different machine learning models."
    )

elif page == "Visualization":
    st.title("Visualization Page")

    # Plot Dollar over time
    st.subheader("Dollar Price Over Time")
    fig_dollar = px.line(df, x='Date', y='Dollar', title='Dollar Price Trends Over Time')
    st.plotly_chart(fig_dollar)

    # Plot Petrol over time
    st.subheader("Petrol Price Over Time")
    fig_petrol = px.line(df, x='Date', y='Petrol', title='Petrol Price Trends Over Time')
    st.plotly_chart(fig_petrol)

    # Plot Crude over time
    st.subheader("Crude Price Over Time")
    fig_crude = px.line(df, x='Date', y='Crude', title='Crude Price Trends Over Time')
    st.plotly_chart(fig_crude)

    # Plot Diesel over time
    st.subheader("Diesel Price Over Time")
    fig_diesel = px.line(df, x='Date', y='Diesel', title='Diesel Price Trends Over Time')
    st.plotly_chart(fig_diesel)


elif page == "Predictions":
    st.title("Predictions Page")

    # Assuming df is already loaded with the dataset

    # Split the data into features (X) and target variables (y)
    X = df[['Dollar', 'Crude']]
    y_petrol = df['Petrol']
    y_diesel = df['Diesel']

    # Train the Neural Network model on the entire dataset
    model_neural_network_petrol = MLPRegressor(max_iter=1000)
    model_neural_network_petrol.fit(X, y_petrol)

    model_neural_network_diesel = MLPRegressor(max_iter=1000)
    model_neural_network_diesel.fit(X, y_diesel)

    # Train the Random Forest model on the entire dataset
    model_random_forest_petrol = RandomForestRegressor()
    model_random_forest_petrol.fit(X, y_petrol)

    model_random_forest_diesel = RandomForestRegressor()
    model_random_forest_diesel.fit(X, y_diesel)

    # User input for Dollar Rate and Crude Price
    dollar_rate = st.slider("Select Dollar Rate for Prediction", min_value=df['Dollar'].min(), max_value=df['Dollar'].max(), step=0.1)
    crude_price = st.slider("Select Crude Price for Prediction", min_value=df['Crude'].min(), max_value=df['Crude'].max(), step=1.0)

    # Make predictions using Neural Network
    pred_neural_network_petrol = model_neural_network_petrol.predict([[dollar_rate, crude_price]])
    pred_neural_network_diesel = model_neural_network_diesel.predict([[dollar_rate, crude_price]])

    # Make predictions using Random Forest
    pred_random_forest_petrol = model_random_forest_petrol.predict([[dollar_rate, crude_price]])
    pred_random_forest_diesel = model_random_forest_diesel.predict([[dollar_rate, crude_price]])

    # Display predictions
    st.subheader("Predictions for Next Month:")
    st.write(f"Neural Network Predicted Petrol Price: {pred_neural_network_petrol[0]:.2f}")
    st.write(f"Neural Network Predicted Diesel Price: {pred_neural_network_diesel[0]:.2f}")
    st.write(f"Random Forest Predicted Petrol Price: {pred_random_forest_petrol[0]:.2f}")
    st.write(f"Random Forest Predicted Diesel Price: {pred_random_forest_diesel[0]:.2f}")

    
