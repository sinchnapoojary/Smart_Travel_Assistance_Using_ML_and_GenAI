import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

# Load the trained model
model = load_model('crowd_prediction_model.h5')

# Load the scaler
scaler = joblib.load('scaler.pkl')

# Example: Load new data for prediction
new_data = pd.DataFrame({
    'temperature (°C)': [30],
    'humidity (%)': [60],
    'wind_speed (km/h)': [15],
})

# Preprocess the data to match the training format
new_data = new_data.values  # Convert to NumPy array
new_data = scaler.transform(new_data)  # Apply the scaler to the new data

# Make predictions
predictions = model.predict(new_data)
predicted_crowd_percentage = predictions[0][0] * 100
print(f"Predicted Crowd Level: {predicted_crowd_percentage:.2f}%")

# To evaluate the model and display MSE
# Example feature data for MSE evaluation (this should be the test set from your training phase)
X_test = np.array([[30, 60, 15]])  # This is just an example; replace with actual test data
y_test = np.array([1])  # Replace with actual target values from the test set

# Normalize the test data
X_test_scaled = scaler.transform(X_test)

# Evaluate the model accuracy (MSE)
loss, mse = model.evaluate(X_test_scaled, y_test, verbose=0)

# Print the MSE for evaluation
print(f"Model Evaluation MSE: {mse:.4f}")

