import requests
from bs4 import BeautifulSoup
	
def get_html( url ):
	respons = requests.get( url )
	return respons.text

def parse( html ):
	soup = BeautifulSoup( html, 'lxml' )
	tds = soup.find( class_="row tile_count" )
	a_p = []
	for row in tds.find_all( class_="count" ):
		a_p.append( row.text )
	return a_p
	#print('Ethereum Gas Prices:\n\nLow speed tx = {3} gwei or {2} USD\nNormal speed tx = {1} gwei or {0} USD\nWaiting time = {4} sec or {5} blocks'.format(a_p[0][1:], a_p[1], a_p[2][1:], a_p[3], a_p[4], a_p[5] ) )

def main():
	print( parse( get_html( 'https://ethgasstation.info' ) ) ) #'https://ethgasstation.info'

if __name__ == '__main__':
	main()