import requests
import re

def getHuluSummaries():
	'''
	Get plot summaries from ihulu.com.
	Similar to itunes, everyhting is in a javascript object appended to the page.
	'''
	r = requests.get('https://www.hulu.com/series/buffy-the-vampire-slayer-f2c277c5-62b4-417c-b277-8435b70176dd?entity_id=01457cec-cdce-488e-998a-bb16f35fe326')
	page = r.text
	
	summaries = re.findall('"type":"episode","name":"[^\{\}\[\]]*","description":"[^\{\}\[\]]*","rating"',page)
	summaries.extend( re.findall('"type":"extra","name":"[^\{\}\[\]]*","description":"[^\{\}\[\]]*","rating"',page) )
	
	#print (len(summaries))
	print("hulu.com: Found %i episodes." % len(summaries))
	trimmed_summaries = []
	for summary in summaries:
		summary = re.search('description":"[^\{\}\[\]]*","', summary).group()
		
		summary = summary[14:-3]
		trimmed_summaries.append(summary)
	return trimmed_summaries
	print (summaries)