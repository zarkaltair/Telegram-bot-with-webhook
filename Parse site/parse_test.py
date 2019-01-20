import requests
from bs4 import BeautifulSoup
	
def get_html(url):
	respons = requests.get(url)
	return respons.text

def parse(html):
	xml = BeautifulSoup(html, 'lxml')
	celebrations = xml.find(class_="listing_wr")
	celebration = []
	for row in celebrations.find_all(itemprop="text"):
		celebration.append(row.text)
	return '\n'.join(celebration)

def main():
	print(parse(get_html('http://kakoysegodnyaprazdnik.ru/')))

if __name__ == '__main__':
	main()