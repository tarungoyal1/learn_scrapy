import requests

from bs4 import BeautifulSoup


headers = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  			'Accept-Language': 'en',
  			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
  		  }
response  = requests.get("https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275",headers=headers)
soup = BeautifulSoup(response.text, 'lxml')


url = soup.find_all('img', {'class':'a-dynamic-image'})[0].attrs['data-a-dynamic-image'].partition(':[')[0][2:-1]

print(url)