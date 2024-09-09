import requests
from .models import Game

def fetch_games():
    url = "https://rawg-video-games-database.p.rapidapi.com/games"
    headers = {
        "x-rapidapi-key": "cb5fadfba7msh807f17f55e2e914p1cf5d9jsne86a10a34850",
        "x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com"
    }
    params = {
        "key": "8cf3a81e6fe7452b9228249eafd7d334"
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    
    for game in data.get('results', []):
        print(game.get('background_image'))
        Game.objects.update_or_create(
            title = game.get('name'),
            defaults={
                'genre': ', '.join([genre['name'] for genre in game.get('genres', [])]),
                'developer': ', '.join([developer['name'] for developer in game.get('developers', [])]),
                'publisher': ', '.join([publisher['name'] for publisher in game.get('publishers', [])]),
                'platform': ', '.join([platform['platform']['name'] for platform in game.get('platforms', [])]),
                'release_date': game.get('released'),
                'image_link': game.get('background_image', ''),
                'exclusive': False  # Adjust as necessary
            }
        )