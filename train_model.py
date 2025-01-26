import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Dropout # type: ignore
import joblib
import matplotlib.pyplot as plt

# Load the preprocessed dataset
file_path = 'C:\Users\shrih\OneDrive\Desktop\FINAL_YEAR_PROJ\preprocessed_dataset.csv'  # Replace with your preprocessed dataset path
data = pd.read_csv(file_path)

# Separate features (X) and target (y)
X = data[['temperature (°C)', 'humidity (%)', 'wind_speed (km/h)']].values

# Clean column names by removing units (optional)
data.columns = data.columns.str.replace(r'\s\(.+\)', '', regex=True)

# Now you can reference columns without units
X = data[['temperature', 'humidity', 'wind_speed']].values
y = data['crowd_level'].values  # Use 'crowd_level' instead of 'crowd_percentage'

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data using MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save the scaler for use in prediction
joblib.dump(scaler, 'scaler.pkl')

# Define the ANN model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(1, activation='linear')  # Output layer for regression
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mse'])

# Train the model
history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=50,
    batch_size=32,
    verbose=1
)

# Save the trained model
model.save('crowd_prediction_model.h5')

# Evaluate the model after training
loss, mse = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Mean Squared Error (MSE): {mse}")  # This should be displayed in your terminal

# Plot training history (optional)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.title('Training History')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()

# Ensure the evaluation message appears:
print(f"Model evaluation completed. Mean Squared Error (MSE): {mse}")
