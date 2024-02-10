import requests
from .models import Animal
import os


def fetch_animals( pages=1):
    url = "https://api.petfinder.com/v2/animals"
    headers = {
        "Authorization": f"Bearer {os.environ.get('PETFINDER_API_KEY')}"
    }
    animals =[]

    for page in range(1, pages +1):
        params = {'page': page}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        animals.extend(data['animals'])

    return animals

animals_data = fetch_animals( pages=10)