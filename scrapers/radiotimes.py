import requests
import re
import sneakyrequest
from bs4 import BeautifulSoup
import time
import json
import pprint
import random

def getRadioTimesSummaries():
	'''
	Get plot summaries from radiotimes.com
	This site is kind of a pain, but it's totally worth it, giving multiple summaries for each episode wrapped in a neat JSON object.
	
	The pages which list each season only give 4 episodes at a time, and the summaries are truncated.
	but if you can get the episode id string, you can request the full JSON object for each episode.
	
	'''
	pp = pprint.PrettyPrinter(indent=4)
	summaries = []
	
	
	for season in range (1,8):
		for part in range (1,8):
			episode_ids = []
			if(season == 1 and part > 4 ):
				break
			
			print ("RadioTimes: Getting episode ids for season %i, part %i..." % (season, part))
			r = requests.get('https://www.radiotimes.com/tv-programme/e/zy9/buffy-the-vampire-slayer-episode-guide/series-%i/%i/' %(season, part))
			time.sleep(random.randrange(4))
			page = r.text
	
			soup = BeautifulSoup(page,'html.parser')
	
			episodes = soup.find_all('a',{'class':'episode-list__item'})
		
			for episode in episodes:
				episode_id = episode['data-episode-id']
				episode_ids.append(episode_id)
			
			print ("RadioTimes: Retrieved %i episode ids" % len(episode_ids))
	
			
			for i in range(len(episode_ids)):
				episode_id = episode_ids[i]
				print("		Getting episode info for #%i" % i)
				r = requests.get('https://immediate-prod.apigee.net/broadcast-content/1/episodes/%s?' % episode_id)
				time.sleep(random.randrange(4))
				page = r.text
				episode_object = json.loads(page)
				#pp.pprint(episode_object)
				if i == 0 and part == 1:
					summaries.append(episode_object['series']['description'])
				try:
					summaries.append(episode_object['short_description'])
					summaries.append(episode_object['medium_description'])
					summaries.append(episode_object['long_description'])
				except:
					print ("RadioTimes: description tags missing form JSON object! missing!")
				
	
		print("RadioTimes: got %i summaries so far." % len(summaries))
		
	
	print ("RadioTime: Got %i summaries" % len(summaries))
	return summaries