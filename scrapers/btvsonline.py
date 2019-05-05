import requests
import re
from bs4 import BeautifulSoup
import lxml


def getBtvsOnlineSummaries():
	'''
	Get plot summaries from btvs.com.
	One page has all summaries. 
	
	'''
	summaries = []
	r = requests.get('http://www.btvsonline.com/episode-guide/')
	page = r.text
	soup = BeautifulSoup(page, 'lxml')
	
	
	ptags = soup.findAll('p')
	for ptag in ptags:
		summary = ptag.getText()
		summary = summary.replace('\n'," ").replace('\r', " ") # remove extra line breaks
		
		#remove text in parentheses
		summary = re.sub("[\(\[].*?[\)\]]", "", summary)
		summary = "".join(summary.split(' — ')[1:])
		if len(summary) > 5:
			summaries.append(summary)
	
	print("btvsonline.com: found %i summaries total." % len(summaries))
	return (summaries)