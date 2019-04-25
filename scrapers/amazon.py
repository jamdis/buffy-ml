import requests
from sneakyrequest import sneakyRequest
from bs4 import BeautifulSoup


def getAmazonSummaries():
	'''
	Amazon hates people scraping their pages. But using their api requires signing up with a credit card.
	Fuck that. 
	Instead, this makes repeated attempts with random proxies and browser id strings , and repeats until it gets every episode.
	'''
	season_page_ids = ['B000HCTDC2', 'B00EU7XZ4W', 'B00ET0YAK8', 'B00EU7W16K', 'B00ET0VVFK', 'B00EU7UTVE', 'B00ET13QZM']
	
	summaries = []
	for i in range(1,8):
		print ("Amazon: Getting Season %i" % i)
		url = 'https://www.amazon.com/gp/product/%s' % season_page_ids[i-1]
		page = sneakyRequest(url)
		
		if type(i) != None:
			print (page)
			print("Amazon: Something isn't working")
		
			soup = BeautifulSoup(page,'html.parser')
			episodes = soup.find_all('div',{'class':'_1YOcuW'})
			
			for episode in episodes:
				summary = episode.get_text()
				summaries.append(summary)
	return summaries
			
			
