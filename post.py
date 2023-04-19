import requests

payload = {'x': 52, 'y': 20, 'color': 'r'}
#response = requests.post('http://pb.dmcraft.online', data=payload)
response = requests.post('http://127.0.0.1:3333', data=payload)
print(response)
