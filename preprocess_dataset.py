import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pickle

# Load the dataset
file_path = 'C:\Users\shrih\OneDrive\Desktop\FINAL_YEAR_PROJ\extended_travel_planner_data_25000_ballari.csv'
data = pd.read_csv(file_path)

# Step 1: Create a target variable (crowd level)
data['crowd_level'] = (0.5 * data['temperature (°C)']) + \
                      (0.3 * data['humidity (%)']) - \
                      (0.2 * data['wind_speed (km/h)'])
data['crowd_level'] = data['crowd_level'].clip(lower=0, upper=100)

# Step 2: One-hot encode the weather column
weather_encoded = pd.get_dummies(data['weather'], prefix='weather')
data = pd.concat([data, weather_encoded], axis=1)
data.drop(columns=['weather'], inplace=True)

# Step 3: Normalize features and target
features = ['temperature (°C)', 'humidity (%)', 'wind_speed (km/h)'] + list(weather_encoded.columns)
scaler = MinMaxScaler()
data[features] = scaler.fit_transform(data[features])

# Save the scaler for real-time predictions
with open('feature_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

target_scaler = MinMaxScaler()
data[['crowd_level']] = target_scaler.fit_transform(data[['crowd_level']])
with open('target_scaler.pkl', 'wb') as f:
    pickle.dump(target_scaler, f)

# Save the preprocessed dataset
data.to_csv('preprocessed_dataset.csv', index=False)
print("Dataset preprocessed and saved!")
print(data.columns)