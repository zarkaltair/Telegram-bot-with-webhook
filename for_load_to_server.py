import requests
import re
import pyowm
import datetime
from bs4 import BeautifulSoup


def get_html( url ):
	respons = requests.get( url )
	html = respons.text
	return html

def parse( html ):
	soup = BeautifulSoup( html, 'lxml' )
	string = soup.find( class_="row tile_count" )
	a_p = []
	for row in string.find_all( class_="count" ):
		a_p.append( row.text )
	return 'Ethereum Gas Prices\n\nLow speed tx = {3} gwei or {2} USD\nNormal speed tx = {1} gwei or {0} USD\nWaiting time = {4} sec or {5} blocks'.format(a_p[0][1:], a_p[1], a_p[2][1:], a_p[3], a_p[4], a_p[5] )

def parse_text( text ):
	pattern = r'/\w+'
	crypto  = re.search( pattern, text ).group()
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
		return 'Top 10 cryptocurrency in USD\n\n1. {0:20}${1}\n2. {2:20}${3}\n3. {4:20}${5}\n4. {6:20}${7}\n5. {8:20}${9}\n6. {10:20}${11}\n7. {12:20}${13}\n8. {14:20}${15}\n9. {16:20}${17}\n10.{18:20}${19}'.format(n_1, p_1, n_2, p_2, n_3, p_3, n_4, p_4, n_5, p_5, n_6, p_6, n_7, p_7, n_8, p_8, n_9, p_9, n_10, p_10)

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
		owm         = pyowm.OWM                 ( '70732ac514bf006244ac74c5f31de5aa', language='ru' )
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
		temp_M      = w_M.get_temperature       ( 'celsius' ) ['temp']
		temp_E      = w_E.get_temperature       ( 'celsius' ) ['temp']
		temp_O      = w_O.get_temperature       ( 'celsius' ) ['temp']
		temp_P      = w_P.get_temperature       ( 'celsius' ) ['temp']
		temp_S      = w_S.get_temperature       ( 'celsius' ) ['temp']
		wind_M      = w_M.get_wind              () ['speed']
		wind_E      = w_E.get_wind              () ['speed']
		wind_O      = w_O.get_wind              () ['speed']
		wind_P      = w_P.get_wind              () ['speed']
		wind_S      = w_S.get_wind              () ['speed']
		status_M    = w_M.get_detailed_status   ()
		status_E    = w_E.get_detailed_status   ()
		status_O    = w_O.get_detailed_status   ()
		status_P    = w_P.get_detailed_status   ()
		status_S    = w_S.get_detailed_status   ()
		return 'Москва {0} °C, {1}, ветер {2} м/с.\nЕкатеринбург {3} °C, {4}, ветер {5} м/с.\nОмск {6} °C, {7}, ветер {8} м/с.\nПетухово {9} °C, {10}, ветер {11} м/с.\nШерегеш {12} °C, {13}, ветер {14} м/с.'.format( temp_M, status_M, wind_M, temp_E, status_E, wind_E, temp_O, status_O, wind_O, temp_P, status_P, wind_P, temp_S, status_S, wind_S )
#		return 'Погода в Москве {0} °C, {1}, скорость ветра {2} м/с.\nПогода в Екатеринбурге {3} °C, {4}, скорость ветра {5} м/с.\nПогода в Омске {6} °C, {7}, скорость ветра {8} м/с.\nПогода в Петухово {9} °C, {10}, скорость ветра {11} м/с.\nПогода в Шерегеше {12} °C, {13}, скорость ветра {14} м/с.'.format( temp_M, status_M, wind_M, temp_E, status_E, wind_E, temp_O, status_O, wind_O, temp_P, status_P, wind_P, temp_S, status_S, wind_S )

	elif crypto == 'test': 
		return 'This is the test message.'

	elif crypto == 'new_year':
		countdown = lambda : datetime.datetime(2019,1,1,00,00) - datetime.datetime.now()
		return 'До нового года осталось:\n' + str(countdown())

	else: 
		url        = 'https://api.coinmarketcap.com/v1/ticker/{}'.format( crypto ) 
		result     = requests.get( url ).json() 
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
		message    = '{0:20}{1}\n{2:20}#{3}\n{4:20}{5}\n{6:20}${7}\n{8:20}${9}\n{10:20}{11}%\n{12:20}{13}%\n{14:20}{15}%'.format('Coin name:', name,'Market ticker:', symbol, 'Price BTC:', price_btc, 'Price USD:', price, 'Market cap:', market, 'Change 1h:', change_1h, 'Change 24h:', change_24h, 'Change 7d:', change_7d )
		return message 

def main():
	print( get_price( parse_text( '/new_year' ) ) )

if __name__ == '__main__':
	main()