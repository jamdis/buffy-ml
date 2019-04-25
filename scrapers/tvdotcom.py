import requests
from bs4 import BeautifulSoup

def getTvDotComSummaries():
	'''
	Get plot summaries from tv.com.
	Choosing the 'printable' version of the page gives all summaries on one page!
	'''
	summaries = []
	
	r = requests.get('http://www.tv.com/shows/buffy-the-vampire-slayer/episodes/?printable=1')
	page = r.text
	soup = BeautifulSoup(page,'html.parser')
	episodes = soup.find_all('div',{'class':'description'})

	print("tv.com: Found %i episodes." % len(episodes))
	for episode in episodes:
		summary = (episode.get_text())
		summaries.append(summary)
	return summaries