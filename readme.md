# Fuel Predictor App

The Fuel Predictor App is a tool that allows users to analyze historical fuel price trends and make predictions for future fuel prices using machine learning algorithms. This app provides insights into the relationship between various factors such as the dollar rate, crude oil prices, and the prices of petrol and diesel in Zambia.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Pages](#pages)
  - [Home](#home)
  - [Visualization](#visualization)
  - [Predictions](#predictions)
- [Contributing](#contributing)
- [License](#license)

## Features

- Visualize historical trends of Dollar Rate, Crude Oil Prices, Petrol, and Diesel prices over time.
- Make predictions for future Petrol and Diesel prices based on user inputs for Dollar Rate and Crude Oil Prices.
- Utilize machine learning algorithms, including Neural Networks and Random Forest, for prediction.

## Getting Started

### Prerequisites

- Python (version 3.6 or higher)
- Pip (Python package installer)
- Git

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kshula/fuel-predictor-app.git
    cd fuel-predictor-app
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:

    ```bash
    streamlit run price.py
    ```

## Usage

1. Navigate to the different pages using the sidebar.
2. Explore historical trends on the Visualization page.
3. Make predictions for Petrol and Diesel prices on the Predictions page by adjusting Dollar Rate and Crude Oil Prices sliders.

## Pages

### Home

- Provides an introduction to the Fuel Predictor App and its features.

### Visualization

- Visualizes historical trends of Dollar Rate, Crude Oil Prices, Petrol, and Diesel prices over time.

### Predictions

- Allows users to make predictions for future Petrol and Diesel prices based on user inputs for Dollar Rate and Crude Oil Prices.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

