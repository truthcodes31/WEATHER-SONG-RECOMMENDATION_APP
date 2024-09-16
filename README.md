Weather Song Recommendation App

This project is a Flask-based web application that recommends YouTube music playlists based on the current weather conditions in a specified city. The app fetches weather data from the OpenWeather API and uses the YouTube API to find music playlists that match the weather condition.

video url: "https://youtu.be/46OpFhU56Bo"
Project Structure

E

weather_song_recommendation/
│
├── project.py                  # Main Flask app
├── templates/              # HTML templates
│   ├── index.html
│   └── results.html
├── static/                 # Static assets (if any, e.g., CSS, JS)
├── test project/                  # Directory for test files
│   └── test_project.py         # Unit tests for Flask app
├── requirements.txt        # List of dependencies
└── README.md               # Project description


 Features

- Fetches real-time weather data using the [OpenWeather API](https://openweathermap.org/api).
- Recommends YouTube music playlists based on the weather conditions using the [YouTube Data API](https://developers.google.com/youtube/v3).
- Displays the current weather condition (temperature, humidity, and description) along with clickable YouTube links.

 Prerequisites

- Python 3.7+
- Flask
- API keys for:
  - [OpenWeather](https://openweathermap.org/api)
  - [YouTube Data API](https://developers.google.com/youtube/v3)

 Setup Instructions

1. *Clone the repository:*

    git clone https://github.com/truthcodes31/weather-song-recommendation.git
    cd weather-song-recommendation
    

2. *Install dependencies:*

    First, ensure you have Python and pip installed. Then run:

    bash
    pip install -r requirements.txt
    

3. *Set up API keys:*

    In project.py, replace the placeholders with your own API keys:
    
    python
    YOUTUBE_API_KEY = 'your_youtube_api_key'
    OPENWEATHER_API_KEY = 'your_openweather_api_key'
    

4. *Run the application:*

    After setting up everything, run the Flask development server:

    bash
    python app.py
    

    The app will be available at http://127.0.0.1:5000/.

 Usage

1. Open your browser and go to http://127.0.0.1:5000/.
2. Enter the name of a city in the input field.
3. The application will display the current weather condition and a list of recommended music playlists from YouTube based on the weather.

 Testing

This project includes unit tests using pytest. To run the tests, ensure pytest is installed, then use the following command:

bash
pytest test project/


 Dependencies

- Flask: A micro web framework for Python.
- Requests: Used to make HTTP requests to the OpenWeather API.
- google-api-python-client: Python client library for YouTube API access.
- Pytest: A testing framework for Python.

 Example

- A user enters the city "London".
- The app fetches weather data, determines it’s "Cloudy" with 15°C, and shows recommended YouTube playlists for "Cloudy" weather.



