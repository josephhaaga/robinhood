import requests
import random
HOST = "https://mygeoangelfirespace.city"

a = requests.get(f"{HOST}/db/users.json").json()

sorted(a['users'].values(), key=lambda k: k['street_cred'])

population = len(a['users'].values())

uninsured_users = [x for x in a['users'].values()]
poor_people = sorted(uninsured_users, key = lambda k: k['cool_points'])[:20]

poor_players = [x['name'] for x in poor_people]

target = 'joehaaga'

for player in poor_players:
    print(f'@{player}', end=' ')
