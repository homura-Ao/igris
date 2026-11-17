import requests

token = open('token.txt').read().strip()
r = requests.get('https://api.telegram.org/bot' + token + '/getUpdates')
print(r.json()['result'][0]['message']['chat']['id'])
