import requests
import re
import sneakyrequest
from bs4 import BeautifulSoup

def getVryaSummaries():
	'''
	Get plot summaries from Vrya.net
	All on one page in tds with class 'subtle'
	Need to filter out other 'subtle td's
	
	'''
	summaries = []
	
	
	print ("Vrya: Getting Buffy Summaries...")
	r = requests.get('http://vrya.net/bdb/ep.php')
	page = r.text

	soup = BeautifulSoup(page,'html.parser')
	episodes = soup.find_all('td',{'class':'subtle'})
	print ("Vrya: found %i divs" % len(episodes))
	
	
	for episode in episodes:
		if not episode.get_text().startswith("Ep"):
			summary = episode.get_text()
			summaries.append(summary)
		if  len(summaries) >= 144:
			break
	print ("Vrya: Retrieved %i summaries" % len(summaries))

	return summaries