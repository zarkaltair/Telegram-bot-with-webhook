from flask import Flask
from flask import request
from flask import jsonify
from bs4 import BeautifulSoup
import requests
import re
import pyowm
import datetime


app = Flask(__name__)
URL = 'https://api.telegram.org/bot<api-key>/'

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

def send_message(chat_id, text='123', parse_mode='html'):
	url = URL + 'sendMessage'
	answer = {'chat_id': chat_id, 'text': text, 'parse_mode': 'html'}
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
		return '<code>#Top 10 cryptocurrency in USD\n\n1. {0:15}${1}\n2. {2:15}${3}\n3. {4:15}${5}\n4. {6:15}${7}\n5. {8:15}${9}\n6. {10:15}${11}\n7. {12:15}${13}\n8. {14:15}${15}\n9. {16:15}${17}\n10.{18:15}${19}</code>'.format(n_1, p_1, n_2, p_2, n_3, p_3, n_4, p_4, n_5, p_5, n_6, p_6, n_7, p_7, n_8, p_8, n_9, p_9, n_10, p_10)

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
		town_M      = 'Москва'
		town_E      = 'Екатеринбург'
		town_O      = 'Омск'
		town_P      = 'Петухово'
		town_S      = 'Шерегеш'
		owm         = pyowm.OWM                 ('70732ac514bf006244ac74c5f31de5aa', language='ru')
		obs_M       = owm.weather_at_place      ( town_M )
		obs_E       = owm.weather_at_place      ( town_E )
		obs_O       = owm.weather_at_place      ( town_O )
		obs_P       = owm.weather_at_place      ( town_P )
		obs_S       = owm.weather_at_place      ( town_S )
		w_M         = obs_M.get_weather         ()
		w_E         = obs_E.get_weather         ()
		w_O         = obs_O.get_weather         ()
		w_P         = obs_P.get_weather         ()
		w_S         = obs_S.get_weather         ()
		temp_M      = w_M.get_temperature       ('celsius') ['temp']
		temp_M = round(temp_M)
		temp_E      = w_E.get_temperature       ('celsius') ['temp']
		temp_E = round(temp_E)
		temp_O      = w_O.get_temperature       ('celsius') ['temp']
		temp_O = round(temp_O)
		temp_P      = w_P.get_temperature       ('celsius') ['temp']
		temp_P = round(temp_P)
		temp_S      = w_S.get_temperature       ('celsius') ['temp']
		temp_S = round(temp_S)
		wind_M      = w_M.get_wind              () ['speed']
		wind_M = round(wind_M)
		wind_E      = w_E.get_wind              () ['speed']
		wind_E = round(wind_E)
		wind_O      = w_O.get_wind              () ['speed']
		wind_O = round(wind_O)
		wind_P      = w_P.get_wind              () ['speed']
		wind_P = round(wind_P)
		wind_S      = w_S.get_wind              () ['speed']
		wind_S = round(wind_S)
		status_M    = w_M.get_detailed_status   ()
		status_E    = w_E.get_detailed_status   ()
		status_O    = w_O.get_detailed_status   ()
		status_P    = w_P.get_detailed_status   ()
		status_S    = w_S.get_detailed_status   ()
		return '<b>Москва:</b>\nt: {0}, w: {2:2} м/с, {1}.\n<b>Екатеринбург:</b>\nt: {3}, w: {5} м/с, {4}.\n<b>Омск:</b>\nt: {6}, w: {8} м/с, {7}.\n<b>Петухово:</b>\nt: {9}, w: {11} м/с, {10}.\n<b>Шерегеш:</b>\nt: {12}, w: {14:2} м/с, {13}.'.format( str(temp_M) + '°C', status_M, wind_M, str(temp_E) + '°C', status_E, wind_E, str(temp_O) + '°C', status_O, wind_O, str(temp_P) + '°C', status_P, wind_P, str(temp_S) + '°C', status_S, wind_S )

	elif crypto == 'new_year':
	    countdown = lambda : datetime.datetime(2019,1,1,00,00) - datetime.datetime.now().replace(microsecond=0)
	    return '<code>New year is coming\n' + str(countdown()) + '</code>'

	elif crypto == 'test':
	    return '<b>This is the test message.</b>'

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
		message    = '<code>{0:16}{1}\n{2:16}#{3}\n{4:16}{5}\n{6:16}${7}\n{8:16}${9}\n{10:16}{11}%\n{12:16}{13}%\n{14:16}{15}%</code>'.format('Coin name:', name,'Market ticker:', symbol, 'Price BTC:', price_btc, 'Price USD:', price, 'Market cap:', market, 'Change 1h:', change_1h, 'Change 24h:', change_24h, 'Change 7d:', change_7d )
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
			send_message(chat_id, text=price, parse_mode='html')
		return jsonify(r)
	return '<h1>Bot welcomes you</h1>'

if __name__ == '__name__':
	app.run()