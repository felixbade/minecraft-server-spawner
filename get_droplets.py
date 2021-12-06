import json
from pprint import pprint
import os

import requests
from beautifultable import BeautifulTable
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

droplets = get_droplets()
table = BeautifulTable()

for droplet in droplets:
    name = droplet['name']
    price = droplet['size']['price_monthly']
    price_s = '{:.2f} €/mo'.format(price)
    networkv4 = droplet['networks']['v4']
    ipv4_address = [x for x in networkv4 if x['type'] == 'public'][0]['ip_address']
    table.rows.append([name, ipv4_address, price_s])

table.set_style(BeautifulTable.STYLE_NONE)
table.columns.alignment = BeautifulTable.ALIGN_LEFT
table.columns.padding_left = 0
table.columns.padding_right = 2
table.columns.alignment[2] = BeautifulTable.ALIGN_RIGHT
print(table)
