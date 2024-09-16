import pytest
from project import project

@pytest.fixture
def client():
    with project.test_client() as client:
        yield client

def test_index_page(client):
    """Test if the index page is accessible."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Weather Song Recommendations" in response.data

def test_get_recommendations(client, monkeypatch):
    """Test the recommendation route with mock data."""
    # Mock weather data
    mock_weather_data = {
        'weather': [{'main': 'Clear'}],
        'main': {'temp': 30, 'humidity': 40}
    }
    
    # Mock YouTube recommendation data
    mock_youtube_recommendations = ['Sunny Day Song - https://youtu.be/12345']
    
    # Monkeypatch functions to return mock data
    def mock_get_weather_data(city, api_key):
        return mock_weather_data

    def mock_get_youtube_recommendations(weather_category):
        return mock_youtube_recommendations
    
    monkeypatch.setattr('project.get_weather_data', mock_get_weather_data)
    monkeypatch.setattr('project.get_youtube_recommendations', mock_get_youtube_recommendations)
    
    # Send POST request
    response = client.post('/get_recommendations', data={'city': 'London'})
    
    assert response.status_code == 200
    assert b"Sunny Day Song" in response.data
    assert b"https://youtu.be/12345" in response.data
