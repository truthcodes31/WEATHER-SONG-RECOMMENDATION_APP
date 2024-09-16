from flask import Flask, render_template, request
import requests
from googleapiclient.discovery import build

project = Flask(__name__, template_folder='templates')


YOUTUBE_API_KEY = 'AIzaSyCA6SOI3XvPFz2T1_rPB8wBXlJalQ85Ey4'  


def get_weather_data(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()


def categorize_weather(weather_data):
    condition = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']

    if condition == 'Clear' and temp > 25:
        return 'Sunny'
    elif 'Rain' in condition:
        return 'Rainy'
    elif condition == 'Clouds':
        return 'Cloudy'
    elif 'Snow' in condition:
        return 'Snowy'
    else:
        return 'Windy'


def get_youtube_recommendations(weather_category):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    
    search_query = f"{weather_category} music playlist"
    request = youtube.search().list(
        q=search_query,
        part='snippet',
        type='video',
        maxResults=5
    )
    response = request.execute()

    
    videos = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        video_url = f"https://youtu.be/{video_id}"
        videos.append(f"{video_title} - {video_url}")
    
    return videos



@project.route('/')
def index():
    print("Loading index.html")
    return render_template('index.html')

@project.route('/get_recommendations', methods=['POST'])

def get_recommendations():
    city = request.form['city']
    api_key = 'e87f1bd584adfa25778de92eed7f45fa'  # Your OpenWeather API key

    # Ask what the weather is in your city!
    weather_data = get_weather_data(city, api_key)
    category = categorize_weather(weather_data)

    # Extract additional weather details
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']

    # Get the perfect music for the weather from YouTube!
    recommendations = get_youtube_recommendations(category)

    return render_template('index.html', city=city, category=category, 
                           temperature=temperature, humidity=humidity, 
                           description=description, recommendations=recommendations)


if __name__ == '__main__':
    project.run(debug=True)
