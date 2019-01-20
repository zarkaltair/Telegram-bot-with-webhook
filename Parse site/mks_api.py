import requests


url = 'http://api.open-notify.org/iss-now.json'
url = 'http://api.open-notify.org/astros.json'
# url = 'http://api.open-notify.org/iss-pass.json'

def get_json(url):
	r = requests.get(url).json()
	return r

def main():
	print(get_json(url))

if __name__ == '__main__':
	main()