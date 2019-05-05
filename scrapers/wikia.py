import requests
import bs4
from bs4 import BeautifulSoup
import re
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

def getWikiaSummaries():
	'''
	Get plot summaries from Wikia.
	'''
	pages = []
	summaries = []
	
	#get list of episode pages
	r = requests.get('https://buffy.fandom.com/wikia.php?controller=ArticlesApi&method=getTop&category=Buffy_the_Vampire_Slayer_episodes')
	response = json.loads(r.text)
	
	for ep in response['items']:
		title = ep['title']
		id = ep['id']
		print (title)
		
		r = requests.get('https://buffy.fandom.com/api/v1/Articles/AsSimpleJson?id=%s' % id)
		response = json.loads(r.text)
		
		section_titles = []
		for section in response['sections']:
			section_titles.append(section['title'])
		if (("Summary" in section_titles) or ("Synopsis" in section_titles)) and ("season" not in title):
			print("keeping")
			pages.append(response)
		else:
			print("skipping")

	
	for page in pages:
		#pp.pprint(page)
		#get the short synopsis always found in paragraph 2 of the article
		try:
			short_summary = page['sections'][1]['content'][0]['text']
			summaries.append(short_summary)
		except:
			print("WIkia: no short summary here.")
		
		get_this = False
		this_level = 0
		for section in page['sections']:
			#print(section['title'], section['level'])
			if (section['title'] == 'Summary') or (section['title'] == 'Synopsis'):
				get_this = True
				this_level = section['level']
			elif get_this and section['level'] > this_level:
				get_this = True
			else:
				get_this = False
			if(get_this):
				for para in section['content']:
					summaries.append(para['text'])

	
	return summaries