from pprint import pprint
from beautifultable import BeautifulTable

from digitalocean import get_droplets

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
