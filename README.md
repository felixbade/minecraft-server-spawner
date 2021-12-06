# Minecraft Server Spawner
This project makes it easy to create and destroy Minecraft servers on DigitalOcean. This way you are only billed by the hours you play – so you can afford the beefy server. The world data is stored on a Volume.

## Usage
- `cp .env.sample .env`
- Add your DigitalOcean API token to `.env`
- Add your SSH key fingerpring to `.env`
- Make a virtualenv if you wish
- `pip install -r requirements`
- `python3 get_droplets.py`
