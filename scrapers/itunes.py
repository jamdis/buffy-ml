import requests
import re

def getITunesSummaries():
	'''
	Get plot summaries from itunes.apple.com.
	Luckily they offer a 'complete series' that has everything on one page!
	this page loads a massive json object at the bottom which it uses to fill in the page.
	This JSON isn't formed in a way python likes, so I'm just using regex here.
	what's nice is that itunes also has the 'motion comic' so we'll grab those for fun.
	'''
	r = requests.get('https://itunes.apple.com/us/tv-season/buffy-the-vampire-slayer-complete-series/id1307173542')
	page = r.text
	r = requests.get('https://itunes.apple.com/us/tv-season/buffy-the-vampire-slayer-season-8-motion-comic/id380739250')
	page = page + r.text
	
	summaries = re.findall('"description":{"standard":"[^\{\}\[\]]*","short',page)
	#print (summaries)
	#print (len(summaries))
	print("itunes.com: Found %i episodes." % len(summaries))
	trimmed_summaries = []
	for summary in summaries:
		summary = summary[27:-8]
		trimmed_summaries.append(summary)
	return trimmed_summaries
