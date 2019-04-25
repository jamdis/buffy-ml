import requests
import re
import sneakyrequest
from bs4 import BeautifulSoup

def getSimpleWikipediaSummaries():
	'''
	Get plot summaries from Simple Wikipedia
	These are almost identical to the ones on wikipedia, but shortened.
	All on one page in td tags with colspan of '6' or '5'
	
	'''
	summaries = []
	
	
	print ("Simple Wikipedia: Getting all at once...")
	r = requests.get('https://simple.wikipedia.org/wiki/List_of_Buffy_the_Vampire_Slayer_episodes')
	page = r.text

	soup = BeautifulSoup(page,'html.parser')
	episodes = soup.find_all('td',{'colspan':'6'})
	episodes.extend(soup.find_all('td', {'colspan':'5'}))
	print ("found %i summaries" % len(episodes))
	
	
	for episode in episodes:
		summary = episode.get_text()
		if (len(summary) > 1): #filter out empty ones
			summaries.append(summary)
	print ("Simple Wikipedia: Retrieved %i summaries (after empty ones filtered out)" % len(summaries))

	return summaries