import requests
from bs4 import BeautifulSoup
from random import choice
import time

from pymongo import MongoClient
client = MongoClient()
db = client.torrent_parser
films = db.films

url = 'http://torrentik.co'

# useragents = open('useragents.txt').read().split('\n')
# useragent = {'User-Agent': choice(useragents)}

def get_html(url, useragent=None, proxies=None):
	""" get the html of pages"""
	r = requests.get(url, headers=useragent, proxies=proxies)
	return r.text

def get_total_pages(html):
	""" get total pages"""
	soup = BeautifulSoup(html, 'lxml')
	pages = soup.find('div', class_='futt').find_all('a')[-2].get('href')
	total_pages = pages.split('/')[-2]
	return total_pages

def get_all_links_pages(total_pages):
	""" get all pages links"""
	base_url = 'http://torrentik.co'
	page_part = '/page/'
	links_pages = []
	for i in range(1, 2): # int(total_pages) + 1
		url = base_url + page_part + str(i)
		links_pages.append(url)
	return links_pages

def get_all_links(links_pages):
	""" get all links"""
	all_links = []
	for link_page in links_pages:
		html = get_html(link_page)
		soup = BeautifulSoup(html, 'lxml')
		links = soup.find_all('div', class_='film_name')
		for i in links:
			link = i.find('a').get('href')
			all_links.append(link)
	return all_links

def get_page_data(all_links):
	""" get the page data"""
	# запрос на количество элементов на странице через консоль браузера
	# document.querySelectorAll('div#dle-content div#basic')
	# inf = []
	for link in all_links:
		try:
			html = get_html(link)
			soup = BeautifulSoup(html, 'lxml')
			title = soup.find('div', class_='film_name').find('h1').text
			size = str(soup.find_all('b')[4])
			magnet = soup.find('a', class_='linkfix').get('href')
			url_torrent = link
			print(url_torrent)
			# description = soup.find('div', class_='dramka2').get_text()
			# torrent = 
			# description_soup = 

			i = {
				'Title': title,
				'Url': url_torrent,
			    'Size': size,
				'Magnet': magnet,
			}
			films.insert_one(i)

			# print('EXCEPT {} is not exist!!!'.format(title))
			# inf.append(i)
		except:
			print('EXCEPT {} is not exist!!!'.format(title))
			continue
	# return inf

print(get_page_data(get_all_links(get_all_links_pages(get_total_pages(get_html(url))))))