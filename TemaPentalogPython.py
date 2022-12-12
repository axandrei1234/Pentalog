from bs4 import BeautifulSoup
import requests
import configparser

yt = "https://www.youtube.com"
dec = requests.get(yt).content.decode('utf8')
soup = BeautifulSoup(dec, 'html.parser')
ytTitle = soup.find('title')
print(ytTitle.string)
print(soup.find('meta',attrs={'name': 'description'}).get('content'))

config = configparser.ConfigParser()
config.read('yt.ini')
print(config['myURL']['ytURL'])





