import requests
from bs4 import BeautifulSoup

def getWikipediaSummaries():
	'''
	Get plot summaries from wikipedia's season pages.
	the wikimedia api is annoying, and wrappers for it are not working, so let's scrape!
	'''
	summaries = []
	
	for i in range(1,8):
		r = requests.get('https://en.wikipedia.org/wiki/Buffy_the_Vampire_Slayer_(season_%i)' % i)
		page = r.text
		soup = BeautifulSoup(page,'html.parser')
		episodes = soup.find_all('td',{'class':'description'})
	
	
		print("Wikipedia: Found %i episodes in season %i." % (len(episodes), i))
		for episode in episodes:
			summary = (episode.get_text())
			summaries.append(summary)
	return summaries