import requests
import re
import sneakyrequest
from bs4 import BeautifulSoup
import time

def getBuffyGuideSummaries():
	'''
	Get plot summaries from buffyguide.com
	This is a fan site.  Should be pretty simple beautifulSoup.com scrape
	
	'''
	summaries = []
	
	
	for season in range (1,8):
		print ("BuffyGuide: Getting season %i" % (season))
		r = requests.get('http://www.buffyguide.com/episodes/episodes%i.shtml' %(season))
		time.sleep(3)
		page = r.text

		soup = BeautifulSoup(page,'html.parser')
		episodes = soup.find_all('div',{'id':'intelliTXT'})
		print ("found %i summaries" % len(episodes))
		
		
		for episode in episodes:
			summary = episode.get_text()
			summaries.append(summary)
	print ("Buffy Guide: Retrieved %i summaries" % len(summaries))

	return summaries