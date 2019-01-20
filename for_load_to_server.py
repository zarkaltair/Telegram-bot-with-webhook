from bs4 import BeautifulSoup
import requests
import re
import pyowm
import datetime


URL_FOR_RATES = 'https://openexchangerates.org/api/latest.json?app_id=3314f836fa864cb39c496105697a6d7f'
glob_per = 0

def get_html(url):
	respons = requests.get(url)
	html = respons.text
	return html

def parse(html):
	if glob_per == 1:
		xml = BeautifulSoup(html, 'lxml')
		strings = xml.find(class_="row tile_count")
		gas_price = []
		for row in strings.find_all(class_="count"):
			gas_price.append(row.text)
		return 'Ethereum Gas Prices\n\nLow speed tx = {3} gwei or {2} USD\nNormal speed tx = {1} gwei or {0} USD\nWaiting time = {4} sec or {5} blocks'.format(gas_price[0][1:], gas_price[1], gas_price[2][1:], gas_price[3], gas_price[4], gas_price[5] )
	
	elif glob_per == 2:
		xml = BeautifulSoup(html, 'lxml')
		strings = xml.find(class_="listing_wr")
		celebrations = []
		for row in strings.find_all(itemprop="text"):
			celebrations.append(row.text)
		return '\n'.join(celebrations)

	else:
		pass

def fib(n):
	a, b = 0, 1
	fibo_series = []
	x = 0
	while x < n:
		fibo_series.append(a)
		a, b = b, a + b
		x += 1
	return 'First ten members fibonacci series\n' + str(fibo_series)

def parse_text(text):
	pattern = r'/\w+'
	crypto = re.search(pattern, text).group()
	return crypto[1:]

def get_price(crypto):
	global glob_per
	if crypto == 'top':
		crypto = 'ticker'
		url = 'https://api.coinmarketcap.com/v1/{}'.format('ticker')
		result = requests.get(url).json()
		n_1 = result[0] ['name']
		p_1 = round(float(result[0] ['price_usd']), 2)
		n_2 = result[1] ['name']
		p_2 = round(float(result[1] ['price_usd']), 2)
		n_3 = result[2] ['name']
		p_3 = round(float(result[2] ['price_usd']), 2)
		n_4 = result[3] ['name']
		p_4 = round(float(result[3] ['price_usd']), 2)
		n_5 = result[4] ['name']
		p_5 = round(float(result[4] ['price_usd']), 2)
		n_6 = result[5] ['name']
		p_6 = round(float(result[5] ['price_usd']), 2)
		n_7 = result[6] ['name']
		p_7 = round(float(result[6] ['price_usd']), 2)
		n_8 = result[7] ['name']
		p_8 = round(float(result[7] ['price_usd']), 2)
		n_9 = result[8] ['name']
		p_9 = round(float(result[8] ['price_usd']), 2)
		n_10 = result[9] ['name']
		p_10 = round(float(result[9] ['price_usd']), 2)
		return 'Top 10 cryptocurrency in USD\n\n1. {0:20}${1}\n2. {2:20}${3}\n3. {4:20}${5}\n4. {6:20}${7}\n5. {8:20}${9}\n6. {10:20}${11}\n7. {12:20}${13}\n8. {14:20}${15}\n9. {16:20}${17}\n10.{18:20}${19}'.format(n_1, p_1, n_2, p_2, n_3, p_3, n_4, p_4, n_5, p_5, n_6, p_6, n_7, p_7, n_8, p_8, n_9, p_9, n_10, p_10)

	elif crypto == 'mk':
		currency = 'USD'
		global_url = 'https://api.coinmarketcap.com/v2/global/?convert=' + currency
		request = requests.get( global_url )
		results = request.json()
		active_currencies = results[ 'data' ][ 'active_cryptocurrencies' ]
		active_markets = results[ 'data' ][ 'active_markets' ]
		bitcoin_percentage = results[ 'data' ][ 'bitcoin_percentage_of_market_cap' ]
		global_cap = int( results[ 'data' ][ 'quotes' ][ currency ][ 'total_market_cap' ] )
		global_volume = int( results[ 'data' ][ 'quotes' ][ currency ][ 'total_volume_24h' ] )
		active_currencies_strings = '{:,}'.format( active_currencies )
		active_markets_string = '{:,}'.format( active_markets )
		global_cap_string = '{:,}'.format( global_cap )
		global_volume_string = '{:,}'.format( global_volume )
		return 'There are currently ' + active_currencies_strings + ' active cryptocurrencies and ' + active_markets_string + ' active markets.\nThe global cap of all cryptos is ' + global_cap_string + ' USD' + ' and the 24h global volume is ' + global_volume_string + ' USD.\nBitcoin\'s total percentage of global cap is ' + str( bitcoin_percentage ) + '%.'

	elif crypto == 'gas':
		glob_per = 1
		return parse(get_html('https://ethgasstation.info'))

	elif crypto == 'celebrations':
		glob_per = 2
		return parse(get_html('http://kakoysegodnyaprazdnik.ru'))

	elif crypto == 'weather':
		town_M = 'Москва'
		town_E = 'Екатеринбург'
		town_O = 'Омск'
		town_P = 'Петухово'
		town_S = 'Шерегеш'
		owm = pyowm.OWM('70732ac514bf006244ac74c5f31de5aa', language='en')
		obs_M = owm.weather_at_place(town_M)
		obs_E = owm.weather_at_place(town_E)
		obs_O = owm.weather_at_place(town_O)
		obs_P = owm.weather_at_place(town_P)
		obs_S = owm.weather_at_place(town_S)
		w_M = obs_M.get_weather()
		w_E = obs_E.get_weather()
		w_O = obs_O.get_weather()
		w_P = obs_P.get_weather()
		w_S = obs_S.get_weather()
		temp_M = w_M.get_temperature('celsius')['temp']
		temp_M = round(temp_M)
		temp_E = w_E.get_temperature('celsius')['temp']
		temp_E = round(temp_E)
		temp_O = w_O.get_temperature('celsius')['temp']
		temp_O = round(temp_O)
		temp_P = w_P.get_temperature('celsius')['temp']
		temp_P = round(temp_P)
		temp_S = w_S.get_temperature('celsius')['temp']
		temp_S = round(temp_S)
		wind_M = w_M.get_wind()['speed']
		wind_M = round(wind_M)
		wind_E = w_E.get_wind()['speed']
		wind_E = round(wind_E)
		wind_O = w_O.get_wind()['speed']
		wind_O = round(wind_O)
		wind_P = w_P.get_wind()['speed']
		wind_P = round(wind_P)
		wind_S = w_S.get_wind()['speed']
		wind_S = round(wind_S)
		status_M = w_M.get_detailed_status()
		status_E = w_E.get_detailed_status()
		status_O = w_O.get_detailed_status()
		status_P = w_P.get_detailed_status()
		status_S = w_S.get_detailed_status()
		return 'Москва:\nt: {0}, w: {2:2} м/с, {1}.\nЕкатеринбург:\nt: {3}, w: {5} м/с, {4}.\nОмск:\nt: {6}, w: {8} м/с, {7}.\nПетухово:\nt: {9}, w: {11} м/с, {10}.\nШерегеш:\nt: {12}, w: {14:2} м/с, {13}.'.format( str(temp_M) + '°C', status_M, wind_M, str(temp_E) + '°C', status_E, wind_E, str(temp_O) + '°C', status_O, wind_O, str(temp_P) + '°C', status_P, wind_P, str(temp_S) + '°C', status_S, wind_S )

	elif crypto == 'test': 
		return 'This is the test message.'

	elif crypto == 'new_year':
		countdown = lambda : datetime.datetime(2019,1,1,00,00) - datetime.datetime.now().replace(microsecond=0)
		return '```До нового года осталось:\n' + str(countdown()) + '```'

	elif crypto == 'fibo10':
		return fib(10)

	elif crypto == 'rates':
		request = requests.get(URL_FOR_RATES).json()
		rub = round(request['rates']['RUB'], 2)
		eur = round(request['rates']['RUB'] / request['rates']['EUR'], 2)
		cny = round(request['rates']['RUB'] / request['rates']['CNY'], 2)
		try_ = round(request['rates']['RUB'] / request['rates']['TRY'], 2)
		thb = round(request['rates']['RUB'] / request['rates']['THB'], 2)
		kzt = round(request['rates']['RUB'] / request['rates']['KZT'], 2)
		return 'Exchange rates in RUB:\n\n1. USD     {0} ₽\n2. EUR     {1} ₽\n3. CNY     {2} ₽\n4. TRY     {3} ₽\n5. THB     {4} ₽\n6. KZT     {5} ₽'.format(rub, eur, cny, try_, thb, kzt)

	else: 
		url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format( crypto )
		result = requests.get(url).json()
		name = result[0] ['name']
		symbol = result[0] ['symbol']
		price_btc = result[0] ['price_btc']
		price_usd = float( result[0] ['price_usd'] )
		price = round( price_usd, 2 )
		market_cap = int( float( result[0] ['market_cap_usd'] ) )
		market = '{:,}'.format( market_cap ) 
		change_1h = result[0] ['percent_change_1h']
		change_24h = result[0] ['percent_change_24h']
		change_7d = result[0] ['percent_change_7d']
		message = '{0:20}{1}\n{2:20}#{3}\n{4:20}{5}\n{6:20}${7}\n{8:20}${9}\n{10:20}{11}%\n{12:20}{13}%\n{14:20}{15}%'.format('Coin name:', name,'Market ticker:', symbol, 'Price BTC:', price_btc, 'Price USD:', price, 'Market cap:', market, 'Change 1h:', change_1h, 'Change 24h:', change_24h, 'Change 7d:', change_7d )
		return message 

def main():
	print(get_price(parse_text('/rates')))

if __name__ == '__main__':
	main()