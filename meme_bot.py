import os
import requests
from random import choice

token = open('token.txt').read().strip()
chat_id = open('chat_id.txt').read().strip()

captions = ['Delivered by Igris.', 'You have been memed!', 'Midnight special.', 'You\'re very welcome.','Yes. Not all heroes wear capes. And I don\'t.']
pics = [p for p in os.listdir('memes') if p.lower().endswith(('.jpg', '.jpeg', '.png'))]
pic = choice(pics)

url = 'https://api.telegram.org/bot' + token + '/sendPhoto'
with open('memes/' + pic, 'rb') as f:
    r = requests.post(url, data={'chat_id': chat_id, 'caption': choice(captions)}, files={'photo': f})
print(r.json()['ok'])
