import requests
from bs4 import BeautifulSoup
import re


site = 'https://www.shutterstock.com/search?searchterm=surprised+people&search_source=base_search_form&language=en&page=1&sort=popular&people_model_released=true&people_number=1&measurement=px&safe=true'
response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')
urls = [img['src'] for img in img_tags]
count = 1
for url in urls:
	filename = 'smiling'+str(count)+'.jpg'
	with open(filename, 'wb') as f:
	    if 'http' not in url: 
	    	url = '{}{}'.format(site, url)
	    response = requests.get(url)
	    f.write(response.content)
	count=count+1
	if count == 100:
		break
