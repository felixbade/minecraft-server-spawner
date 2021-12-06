from random import random

import os

from dotenv import load_dotenv

from digitalocean import create_droplet

load_dotenv()

ssh_key = os.getenv('SSH_KEY_FINGERPRINT')

hostname = 'minecraft'
region = 'fra1' # Frankfurt 1
size = 'c-2' # CPU-Optimized
image = 'ubuntu-20-04-x64'
ssh_keys = [ssh_key]
user_data = open('user_data.txt').read()
volume_uuid = os.getenv('VOLUME_UUID')


response = create_droplet(
        name=hostname,
        region=region,
        size=size,
        image=image,
        user_data=user_data,
        ssh_keys=ssh_keys,
        volumes=[volume_uuid],
        )

from pprint import pprint
pprint(response)