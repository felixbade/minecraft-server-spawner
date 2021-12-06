import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv('DIGITALOCEAN_TOKEN')

def api_get(path):
    url = 'https://api.digitalocean.com/v2/{}'.format(path)
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(api_token)
            }
    response = requests.get(url, headers=headers)
    return json.loads(response.text)

def get_droplets(page=1, per_page=10):
    path = '/droplets?page={}&per_page={}'.format(page, per_page)
    response = api_get(path)
    return response['droplets']
