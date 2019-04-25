import requests
import re
import sneakyrequest
from bs4 import BeautifulSoup

def getTvMazeSummaries():
	'''
	Get plot summaries from TV maze
	this one is easy.  All on one page in divs with class 'description'
	
	'''
	summaries = []
	
	
	print ("TVMaze: Getting Buffy TV show...")
	r = requests.get('http://www.tvmaze.com/shows/427/buffy-the-vampire-slayer/episodeguide')
	print ("TVMaze: Getting Buffy Comic...")
	r2 = requests.get('http://www.tvmaze.com/shows/32017/buffy-the-vampire-slayer-the-motion-comic/episodeguide')
	page = r.text + r2.text

	soup = BeautifulSoup(page,'html.parser')
	episodes = soup.find_all('div',{'class':'description'})
	print ("found %i summaries" % len(episodes))
	
	
	for episode in episodes:
		summary = episode.get_text()
		summaries.append(summary)
	print ("TV Maze: Retrieved %i summaries" % len(summaries))

	return summaries