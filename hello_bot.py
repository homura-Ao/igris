import requests

token = open('token.txt').read().strip()
chat_id = open('chat_id.txt').read().strip()

url = 'https://api.telegram.org/bot' + token + '/sendMessage'
r = requests.post(url, data={'chat_id': chat_id, 'text': 'Hello, Igris is online.'})
print(r.json())
