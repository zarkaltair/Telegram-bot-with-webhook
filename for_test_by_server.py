import requests
import re
import json
from bs4 import BeautifulSoup
from datetime import datetime


def get_html( y ):
	return y
x = 1

def parse_text( text ):
	pattern = r'/\w+'
	crypto  = re.search( pattern, text ).group()
	return crypto[1:]

def get_price( crypto ):
	if crypto == 'gas':
		return get_html( 3 )
	else:
		return 15

def main():
	print( get_html( 2 ) )
	print( get_price( parse_text( '/gas' ) ) )

if __name__ == '__main__':
	main()