import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Loading Dataset
data = pd.read_csv('AQI_Data (1).csv')

# Getting input features and target
X = data[["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]]
y = data["AQI"]

# Creating and training the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Saving the trained model
joblib.dump(model, 'aqi_prediction_model.pkl')

print("Model trained and saved successfully!")