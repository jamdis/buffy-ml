import requests
import re
import sneakyrequest
from bs4 import BeautifulSoup
import time

def getWatchOnlineSummaries():
	'''
	Get plot summaries from watcholine.guide
	This seems to be the same description info used by google search, msn, and a few others
	
	ugh.  the page uses ajax to load a script which in turn uses jquery to replace the contents 
	of a div.
	Okay so we have to:
	1. load the correct url.  insert the season number
	2. do it again with a 2.js instead of 1.js to get the rest of the eps.
	3. extract the episode data using regex
	4. repeat for all seasons.
	
	'''
	summaries = []
	
	
	for season in range (1,8):
		for part in range (1,3):
			print ("WatchOnine: Getting season %i, part %i..." % (season, part))
			r = requests.get('https://www.watchonline.guide/tv-shows/buffy-the-vampire-slayer-1997/%i/episodes/%i.js?page_load_id=64598325438511&template=episode_block&user_id=31117584590390&_=1555861519431' %(season, part))
			time.sleep(3)
			page = r.text
			page = page.replace("\\","")
	
			soup = BeautifulSoup(page,'html.parser')
	
			episodes = soup.find_all('div',{'class':'season-episode__list-content-description'})
		
			for episode in episodes:
				summary = episode.get_text()
				summaries.append(summary[1:-1])
			print (summaries)
	print ("WatchOline: Retrieved %i summaries" % len(summaries))

	return summaries