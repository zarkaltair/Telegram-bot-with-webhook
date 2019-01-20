import requests


URL_FOR_RATES = 'https://openexchangerates.org/api/latest.json?app_id=3314f836fa864cb39c496105697a6d7f'

def main():
	request = requests.get(URL_FOR_RATES).json()
	rub = round(request['rates']['RUB'], 2)
	eur = round(request['rates']['RUB'] / request['rates']['EUR'], 2)
	cny = round(request['rates']['RUB'] / request['rates']['CNY'], 2)
	try_ = round(request['rates']['RUB'] / request['rates']['TRY'], 2)
	thb = round(request['rates']['RUB'] / request['rates']['THB'], 2)
	kzt = round(request['rates']['RUB'] / request['rates']['KZT'], 2)
	print(rub, eur, try_)

if __name__ == '__main__':
	main()