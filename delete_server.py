import sys

from digitalocean import delete_droplet

if len(sys.argv) < 2:
    print('Usage: python {} <droplet-id>'.format(sys.argv[0]))
    exit(1)

droplet_id = sys.argv[1]
print(delete_droplet(droplet_id))