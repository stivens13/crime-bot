# from geopy.geocoders import Nominatim
import requests
import json
from lxml import html
from uszipcode import ZipcodeSearchEngine

search = ZipcodeSearchEngine()


url = 'https://www.neighborhoodscout.com/{}/{}/crime'

state = ''
city = ''

zipcode = search.by_zipcode("10001")
state = zipcode.State
city = zipcode.City.replace(" ", "-")

url = url.format(state, city)




page = requests.get(url)

tree = html.fromstring(page.content)


crime_list = {
	'Crime index:':							'//*[@class="score mountain-meadow"]',
	'Number of violent cases:': 			'//*[@id="data"]/section[1]/div[2]/div[2]/div/div/table/tbody/tr[1]/td[2]/p/strong',
	'Number of property-related cases:':	'//*[@id="data"]/section[1]/div[2]/div[2]/div/div/table/tbody/tr[1]/td[3]/p/strong',
	'Murder:':								'//*[@id="data"]/section[2]/div[5]/div/div/table/tbody/tr[1]/td[2]',
	'Rape:':								'//*[@id="data"]/section[2]/div[5]/div/div/table/tbody/tr[1]/td[3]',
	'Robbery:':								'//*[@id="data"]/section[2]/div[5]/div/div/table/tbody/tr[1]/td[4]',
	'Assault:':								'//*[@id="data"]/section[2]/div[5]/div/div/table/tbody/tr[1]/td[5]'
	
}

other_crimes = {
	'Your chances of becoming victim of a violent crime:': '//*[@id="data"]/section[2]/div[3]/div/div/div[2]/h3/div'
}

for c in crime_list:
	print(c, tree.xpath(crime_list[c])[0].text.split()[0])

for d in other_crimes:
	other_crime = tree.xpath(other_crimes[d])[0].text.replace('\n', " ")

	print(d, other_crime)


