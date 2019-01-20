# TOKEN = '639237490:AAFgastOyZtYYsD9pGg5iNOsVvAOjE5MeFU'


import requests 
proxies = {'http': "socks5://myproxy:9191"}
r = requests.get('http://google.com', proxies=proxies)
print(r)