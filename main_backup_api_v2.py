from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
import re
from flask_sslify import SSLify

app = Flask(__name__)

URL = 'https://api.telegram.org/bot334278198:AAHAHmqSO8k6y7irOS64AkW4PNTMvbB6kH8/'

def write_json(data, filename='answer.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=2, ensure_ascii=False)

def send_message(chat_id, text='123123'):
	url = URL + 'sendMessage'
	answer = {'chat_id': chat_id, 'text': text}
	r = requests.post(url, json=answer)
	return r.json()

def parse_text(text):
	pattern = r'/\w+'
	crypto = re.search(pattern, text).group()
	return crypto[1:]

def get_price(crypto):
	url = 'https://api.coinmarketcap.com/v2/ticker/{}'.format(crypto)
	r = requests.get(url).json()
	price = r['data']['quotes']['USD']['price']
	return price

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.get_json()
		chat_id = r['message']['chat']['id']
		message = r['message']['text']
		pattern = r'/\w+'
		if re.search(pattern, message):
			price = get_price(parse_text(message))
			send_message(chat_id, text=price)
		return jsonify(r)
	return '<h1>Bot welcomes you</h1>'

if __name__ == '__name__':
	app.run()


