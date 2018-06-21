import requests
from bs4 import BeautifulSoup
import re

site = 'https://www.shutterstock.com/search?search_source=base_search_form&language=en&searchterm=passport+photo&image_type=photo'
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
