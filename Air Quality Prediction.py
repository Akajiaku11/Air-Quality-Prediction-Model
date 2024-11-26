import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Step 1: Generate synthetic air quality data for five months
months = ["January", "February", "March", "April", "May"]
np.random.seed(42)  # For reproducibility

data = {
    "Month": months,
    "CO2": np.random.uniform(400, 1000, size=5).round(3),
    "NO2": np.random.uniform(0.01, 0.2, size=5).round(3),
    "SO2": np.random.uniform(0.01, 0.5, size=5).round(3),
    "PM2.5": np.random.uniform(0.01, 0.05, size=5).round(3),
    "AQI_CO": np.random.uniform(0, 150, size=5).round(2),
    "AQI_NO2": np.random.uniform(0, 200, size=5).round(2),
    "AQI_SO2": np.random.uniform(0, 150, size=5).round(2),
}

# Convert data dictionary to a DataFrame
df = pd.DataFrame(data)

# Convert categorical 'Month' data into numeric data
df['Month'] = pd.Categorical(df['Month']).codes

# Display generated synthetic data
print("Synthetic Air Quality Data:")
print(df)

# Step 2: Prepare data for model training
# Features (independent variables) and target variable (AQI values)
X = df[["Month", "CO2", "NO2", "SO2", "PM2.5"]]
y = df[["AQI_CO", "AQI_NO2", "AQI_SO2"]]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 3: Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Step 4: Make predictions and evaluate model performance
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"\nMean Absolute Error: {mae}")

# Step 5: Predict future AQI for a new month (example: June)
future_data = pd.DataFrame({
    "Month": [5],  # For example, "June" could be encoded as 5
    "CO2": [650],  # Replace with actual or expected CO2 level
    "NO2": [0.07],
    "SO2": [0.1],
    "PM2.5": [0.03]
})
future_aqi = model.predict(future_data)
print("\nPredicted AQI for June:", future_aqi)
