
from flask import Flask, render_template, jsonify, redirect, url_for
import tensorflow as tf
import numpy as np
import requests
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__, template_folder='.')

# Load the trained model
model = tf.keras.models.load_model('crowd_prediction_model.h5')

# Weather API details
API_KEY = '795060565c529b1d7340755ac6985115'
BALLARI_CITY = 'Ballari'

def get_weather_data(city='Ballari'):
    try:
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(base_url)
        data = response.json()

        if response.status_code != 200 or 'main' not in data:
            print("Error fetching weather data.")
            return None

        # Extract relevant features
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        return np.array([[temperature, humidity, wind_speed]])
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

@app.route('/')
def home():
    return redirect(url_for('ballari_fort'))

@app.route('/predict_crowd', methods=['GET'])
def predict_crowd():
    try:
        # Fetch real-time weather data
        weather_data = get_weather_data(BALLARI_CITY)
        if weather_data is None:
            return jsonify({'error': 'Could not fetch weather data'}), 500

        # Preprocess data with MinMaxScaler (ensure scaler is consistent with training)
        scaler = MinMaxScaler(feature_range=(0, 1))
        weather_data_scaled = scaler.fit_transform(weather_data)  # Replace .fit with pre-trained scaler

        # Predict using the model
        predicted_crowd = model.predict(weather_data_scaled)[0][0] * 100  # Convert to percentage

        # Generate a message based on the crowd prediction
        if predicted_crowd > 75:
            message = "Crowd levels are predicted to be high. Plan accordingly!"
        elif predicted_crowd > 50:
            message = "Crowd levels are moderate. Enjoy your visit!"
        else:
            message = "Crowd levels are low. It's a great time to visit!"

        print(f"Predicted Crowd Level: {predicted_crowd}%")  # Debugging info in terminal

        return jsonify({
            'predicted_crowd': round(predicted_crowd, 2),
            'message': message
        })
    except Exception as e:
        print(f"Error in prediction: {e}")
        return jsonify({'error': 'Error in prediction'}), 500

@app.route('/ballari_fort')
def ballari_fort():
    prediction_data = requests.get('http://127.0.0.1:5001/predict_crowd').json()
    if prediction_data:
        return render_template(
            'ballari_fort.html',
            crowd_level=prediction_data.get('predicted_crowd', 'N/A'),
            message=prediction_data.get('message', 'No message available.')
        )
    else:
        return render_template(
            'ballari_fort.html',
            crowd_level=None,
            message="Unable to fetch prediction data."
        )

if __name__ == '__main__':
    app.run(debug=False,port=5001)  # Set debug to False for production



import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load the test dataset (replace this with your actual test data)
# Assuming X_test and y_test are already preprocessed and available
try:
    X_test = np.load("X_test.npy")  # Load test features
    y_test = np.load("y_test.npy")  # Load test labels
except Exception as e:
    print(f"Error loading test data: {e}")
    X_test, y_test = None, None

# Load the trained model
model = tf.keras.models.load_model('crowd_prediction_model.h5')

# Evaluate the model accuracy
if X_test is not None and y_test is not None:
    test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)  # Replace 0 with 1 for detailed logs
    print(f"Model Accuracy: {test_accuracy * 100:.2f}%")
else:
    print("Test data not available. Cannot compute accuracy.")

# @app.route('/train_model', methods=['POST'])
# def train_model_route():
#     return get_model_accuracy()

# @app.route('/predict_crowd', methods=['POST'])
# def predict_crowd_route():
#     return get_prediction_accuracy()