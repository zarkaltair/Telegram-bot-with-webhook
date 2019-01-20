import requests
import numpy as np


url = 'https://api.vk.com/method/friends.get?user_id='
method = ''
user_id = '58451062&fields=bdate' # 58451062 9314022
token = '&access_token=91170dc90134fbeb35a8ea7206c1ecb41914e3ac22982f8941d96c90c497a6c66563d062a1871550f1d05'
version = '&v=5.92'

def vk_api(url):
	r = requests.get(url).json()
	lists = r['response']['items']
	arr = []
	for i in lists:
		i.setdefault('bdate', None)
		arr.append([i['first_name'], i['last_name'], i['bdate']])
	return arr

def main():
	URL = url + user_id + token + version
	print(np.array(vk_api(URL)))

if __name__ == '__main__':
	main()