import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Pool

def get_html( url ):
	respons = requests.get( url )
	return respons.text

def get_all_links( html ):
	soup = BeautifulSoup( html, 'lxml' )
	tds = soup.find( 'table', id="currencies" ).find_all( 'td', class_='cyrrency-name' )
	links = []
	for td in tds:
		a = td.find( 'a' ).get( 'href' )
		link = 'https://coinmarketcap.com' + a
		links.append( link )
	print(links)

def get_page_data( html ):
	soup = BeautifulSoup( html, 'lxml' )
	try:
		name = soup.find( 'h1', class_='text-large' ).text.strip()			###
	except:
		name = ''
	try:
		price = soup.find( 'span', id='quote_price' ).text.strip()			###
	except:
		price = ''
	data = { 'name': name, 'price': price }
	return data

def write_csv( data ):
	with open( 'coinmarketcap.csv' 'a' ) as file:
		writer = csv.writer( file )
		writer.writerow( ( data['name'], data['price'] ) )
		print( data['name'], 'parsed' )

def make_all( url ):
	html = get_html( url )
	data = get_page_data( html )
	write.csv( data )

def main():
	start = datetime.now()
	url = 'https://coinmarketcap.com/all/views/all/'
	all_links = get_all_links( get_html( url ) )
	with Pool( 10 ) as p:
		p.map( make_all, all_links )
	end = datetime.now()
	total = end - start
	print( total )

if __name__ == '__main__':
	main()