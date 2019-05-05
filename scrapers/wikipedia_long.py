import requests
import bs4
from bs4 import BeautifulSoup
import re

def getWikipedia_longSummaries():
	'''
	Get plot summaries from wikipedia.  This gets the long plot summaries from each episode page.
	Longer plot summaries are then broken up into individual paragraphs.
	'''
	links = []
	summaries = []
	
	#get list of summary links
	r = requests.get('https://en.wikipedia.org/wiki/List_of_Buffy_the_Vampire_Slayer_episodes')
	page = r.text
	soup = BeautifulSoup(page,'html.parser')
	episodes = soup.find_all('td',{'class':'summary'})
	for episode in episodes:
		link = episode.find('a')['href']
		links.append(link)
	
	#for each link get summary
	for link in links:
		link = 'https://en.wikipedia.org%s' % link
		print("Wikipedia long: Getting page: %s" % link)
		r = requests.get(link)
		page = r.text
		#print(page)
		soup = BeautifulSoup(page,'html.parser')
		
		heading = soup.find('span',{'id':'Plot'})
		if heading is None:
			heading = soup.find('span',{'id':'Summary'})
		if heading is None:
			heading = soup.find('span',{'id':'Plot_synopsis'})
		if heading is None:
			heading = soup.find('span',{'id':'Plot_summary'})
		
		heading = heading.parent
		sibs = heading.next_siblings
		for sib in sibs:
			if sib.name == "h2":
					break
			elif isinstance(sib, bs4.element.Tag):
				summary = sib.get_text()
				summary = re.sub(r'\([^)]*\)', '', summary)
				summary = re.sub(r'\[.*?\]', '', summary)
				summaries.append(summary)
				
	print ("wikipedia long: found %i summary paragraphs" % len(summaries))	
	return summaries