from flask import Flask
from flask import request
from flask import jsonify
from bs4 import BeautifulSoup
import requests
import re
import pyowm
app = Flask(__name__)
URL = 'https://api.telegram.org/bot334278198:AAHAHmqSO8k6y7irOS64AkW4PNTMvbB6kH8/'

def get_html( urll ):
    respons = requests.get( urll )
    html = respons.text
    return html

def parse( html ):
    soup = BeautifulSoup( html, 'lxml' )
    tds = soup.find( class_="row tile_count" )
    a_p = []
    for row in tds.find_all( class_="count" ):
        a_p.append( row.text )
    return 'Ethereum Gas Prices\n\nLow speed tx = {3} gwei or {2} USD\nNormal speed tx = {1} gwei or {0} USD\nWaiting time = {4} sec or {5} blocks'.format(a_p[0][1:], a_p[1], a_p[2][1:], a_p[3], a_p[4], a_p[5] )

def send_message(chat_id, text='123'):
	url = URL + 'sendMessage'
	answer = {'chat_id': chat_id, 'text': text}
	r = requests.post(url, json=answer)
	return r.json()

def parse_text(text):
	pattern = r'/\w+'
	crypto = re.search(pattern, text).group()
	return crypto[1:]

def get_price( crypto ):
	if crypto == 'top':
		crypto = 'ticker'
		url = 'https://api.coinmarketcap.com/v1/{}'.format( 'ticker' )
		result = requests.get( url ).json()
		n_1    = result[0] ['name']
		p_1    = round(float(result[0] ['price_usd']), 2)
		n_2    = result[1] ['name']
		p_2    = round(float(result[1] ['price_usd']), 2)
		n_3    = result[2] ['name']
		p_3    = round(float(result[2] ['price_usd']), 2)
		n_4    = result[3] ['name']
		p_4    = round(float(result[3] ['price_usd']), 2)
		n_5    = result[4] ['name']
		p_5    = round(float(result[4] ['price_usd']), 2)
		n_6    = result[5] ['name']
		p_6    = round(float(result[5] ['price_usd']), 2)
		n_7    = result[6] ['name']
		p_7    = round(float(result[6] ['price_usd']), 2)
		n_8    = result[7] ['name']
		p_8    = round(float(result[7] ['price_usd']), 2)
		n_9    = result[8] ['name']
		p_9    = round(float(result[8] ['price_usd']), 2)
		n_10   = result[9] ['name']
		p_10   = round(float(result[9] ['price_usd']), 2)
		return '#Top 10 cryptocurrency in USD\n\n1. {0:34}${1}\n2. {2:30}${3}\n3. {4:35}${5}\n4. {6:29}${7}\n5. {8:35}${9}\n6. {10:35}${11}\n7. {12:33}${13}\n8. {14:31}${15}\n9. {16:35}${17}\n10.{18:34}${19}'.format(n_1, p_1, n_2, p_2, n_3, p_3, n_4, p_4, n_5, p_5, n_6, p_6, n_7, p_7, n_8, p_8, n_9, p_9, n_10, p_10)

	elif crypto == 'mk':
		currency     = 'USD'
		global_url   = 'https://api.coinmarketcap.com/v2/global/?convert=' + currency
		request      = requests.get( global_url )
		results      = request.json()
		active_currencies    = results[ 'data' ][ 'active_cryptocurrencies' ]
		active_markets       = results[ 'data' ][ 'active_markets' ]
		bitcoin_percentage   = results[ 'data' ][ 'bitcoin_percentage_of_market_cap' ]
		global_cap           = int( results[ 'data' ][ 'quotes' ][ currency ][ 'total_market_cap' ] )
		global_volume        = int( results[ 'data' ][ 'quotes' ][ currency ][ 'total_volume_24h' ] )
		active_currencies_strings     = '{:,}'.format( active_currencies )
		active_markets_string         = '{:,}'.format( active_markets )
		global_cap_string             = '{:,}'.format( global_cap )
		global_volume_string          = '{:,}'.format( global_volume )
		return 'There are currently ' + active_currencies_strings + ' active cryptocurrencies and ' + active_markets_string + ' active markets.\nThe global cap of all cryptos is ' + global_cap_string + ' USD' + ' and the 24h global volume is ' + global_volume_string + ' USD.\nBitcoin\'s total percentage of global cap is ' + str( bitcoin_percentage ) + '%.'

	elif crypto == 'gas':
	    return parse( get_html( 'https://ethgasstation.info' ) )

	elif crypto == 'weather':
		town        = input                     ( 'Какой город Вас интересует?: ' )
		owm         = pyowm.OWM                 ( '70732ac514bf006244ac74c5f31de5aa', language='ru' )
		observation = owm.weather_at_place      ( town )
		w           = observation.get_weather   ()
		temp        = w.get_temperature         ( 'celsius' ) ['temp']
		wind        = w.get_wind                () ['speed']
		status      = w.get_detailed_status     ()
		print( 'Температура в городе ' + town + ' сейчас: ' + str( int( temp ) ) + ' C*' )
		print( 'Также, в указанном городе ' + status )
		print( 'Скорость ветра в городе ' + town + ' сейчас: ' + str( wind ) + ' м/с' )

	elif crypto == 'test':
	    return 'This is the test message.'

	else:
		url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format( crypto )
		result = requests.get( url ).json()
		name       = result[0] ['name']
		symbol     = result[0] ['symbol']
		price_btc  = result[0] ['price_btc']
		price_usd  = float( result[0] ['price_usd'] )
		price      = round( price_usd, 2 )
		market_cap = int( float( result[0] ['market_cap_usd'] ) )
		market     = '{:,}'.format( market_cap )
		change_1h  = result[0] ['percent_change_1h']
		change_24h = result[0] ['percent_change_24h']
		change_7d  = result[0] ['percent_change_7d']
		message    = '{0:26}{1}\n{2:26}#{3}\n{4:28}{5}\n{6:28}${7}\n{8:26}${9}\n{10:26}{11}%\n{12:25}{13}%\n{14:26}{15}%'.format('Coin name:', name,'Market ticker:', symbol, 'Price BTC:', price_btc, 'Price USD:', price, 'Market cap:', market, 'Change 1h:', change_1h, 'Change 24h:', change_24h, 'Change 7d:', change_7d )
		return message

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