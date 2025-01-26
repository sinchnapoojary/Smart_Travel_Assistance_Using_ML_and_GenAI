# TravelSync - Your Smart Travel Companion

## Overview  
**TravelSync** is a smart travel assistance platform powered by **Machine Learning (ML)** and **Generative AI (GenAI)**. It simplifies and enhances travel planning by offering:  
- Real-time data  
- AI-driven recommendations  
- Comprehensive tools for a seamless experience  

Key functionalities include **real-time weather updates**, **crowd density predictions**, **personalized itinerary generation**, and **interactive chatbot assistance**. With geolocation services and dynamic recommendations, **TravelSync** is an intuitive and reliable travel tool.

---

## Features  
1. **Real-Time Weather Tracking**  
   - Accurate and up-to-date weather forecasts.  
2. **Crowd Density Predictions**  
   - Uses Artificial Neural Networks (ANN) trained on historical and real-time data to predict crowd levels.  
3. **Personalized Itinerary Creation**  
   - Generates travel plans based on preferences, optimized routes, and selected attractions.  
4. **AI-Powered Chatbot**  
   - 24/7 assistance for queries, itinerary updates, and general travel information.  
5. **Travel Recommendations for Karnataka**  
   - Highlights key destinations and attractions to boost tourism in Karnataka.  
6. **Emergency Assistance**  
   - Provides local and national emergency contacts for hospitals, police, and more.  
7. **Geolocation Services**  
   - Offers navigation, nearby attractions, and emergency contact information.  
8. **Interactive Maps**  
   - Highlights key attractions, routes, and points of interest using integrated APIs.  

---

## Technology Used  
1. **Frontend**: HTML, CSS, JavaScript  
2. **Backend**: Python (Flask/Django)  
3. **Machine Learning**: TensorFlow/Keras (ANN models)  
4. **Database**: SQLite  
5. **APIs**: OpenWeatherMap  

---

## Dataset  
- **Extended Travel Planner Data**  
  - File: `extended_travel_planner_data_25000_ballari.csv`  
  - Size: 3.63 MB  

---

## Installation and Setup  

### Prerequisites  
- Python 3.10+  
- Virtual Environment (optional but recommended)  

### Steps  
1. **Extract the ZIP File**  
   - Download and extract the `TravelBuddy` folder from the provided ZIP file.  

2. **Set Up Virtual Environment**  
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate     # For Windows
   ```  

3. **Install Dependencies**  
   ```bash
   pip install -r TravelBuddy/Virtual\ Guide/requirements.txt
   ```  

4. **Set Up Environment Variables**  
   - Configure the `.env` file in `Virtual Guide/` with necessary keys.  

5. **Run the Application**  
   ```bash
   python TravelBuddy/Virtual\ Guide/app.py
   ```  

6. **Access the Application**  
   - Ensure Flask applications (`app.py` at `http://127.0.0.1:5001` and `wsgi.py` at `http://127.0.0.1:5000`) are running before launching the project via `travelsync.html`.  

---

## How to Use  

1. **Free and Open Source**  
   - No login is required to access most features.  

2. **Homepage**  
   - Search for destinations or travel places.  
   - Access the chatbot for real-time assistance.  

3. **Destination Search**  
   - Redirects to a page with:  
     - Destination descriptions  
     - Weather information  
     - Recommendations and attractions (mapped with coordinates)  
     - Exploration options for hotels, restaurants, and activities, with real-time crowd predictions.  

4. **Travel Assistant (Virtual Guide)**  
   - Input travel details (duration, dates, start/end locations).  
   - Generates day-wise itineraries with weather forecasts.  
   - Download itineraries in text format for customization.  
   - Logged-in users receive personalized recommendations.  

---

## Project Structure  

1. **Main Directory**  
   - Contains project files, datasets, and scripts.  

2. **Virtual Guide**  
   - Web app implementation, static files, and templates.  

3. **Datasets**  
   - Core data for travel planning.  

4. **Machine Learning**  
   - Scripts for preprocessing, training, and prediction.  

---

## Results  

1. **Weather Tracking**  
   - Delivered accurate updates with an average response time of 200ms.  

2. **Crowd Predictions**  
   - Reliable predictions with low Mean Squared Error (MSE).  

3. **Interactive Features**  
   - User-friendly tools like AI planners and geolocation services.  

4. **Platform Performance**  
   - Optimized load times to under three seconds.  

---

## Future Enhancements  

1. Multi-language support for international users.  
2. Live traffic updates for better route planning.  
3. Expanded data coverage for global locations.  
4. Enhanced ANN models with additional datasets for improved accuracy.  

---

## Project Associates
1. Shreeharsh Joshi
2. Shreyas C
3. Sinchana Poojary
4. Sreevalli R
