import requests
import re

def getTvGuideSummaries():
	'''
	Get plot summaries from ihulu.com.
	Similar to itunes, everything is in a javascript object appended to the page.
	Unfortunately, we do need to load a page for each season
	'''
	summaries = []
	for season in range(1,8):
		r = requests.get('https://www.tvguide.com/tvshows/buffy-the-vampire-slayer/episodes-season-%i/100074/' % season)
		page = r.text
		episodes = 	re.findall('"description": "[^\{\}\[\]:]*\. [A-Z]',page) 
		summaries.extend(episodes)
		#summaries.extend( re.findall('"type":"extra","name":"[^\{\}\[\]]*","description":"[^\{\}\[\]]*","rating"',page) )
	
		#print (len(summaries))
		print("tvguide.com: Found %i episodes in season %i." % (len(episodes), season))
	print("tvguide.com: found %i summaries total." % len(summaries))
	trimmed_summaries = []
	for summary in summaries:
		summary = summary[16:-2]
		trimmed_summaries.append(summary)
	return (trimmed_summaries)