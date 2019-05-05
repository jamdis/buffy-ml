import requests
import re
from bs4 import BeautifulSoup
import lxml


def getChosenTwoSummaries():
	'''
	Get plot summaries from ChosenTwo.com.
	One page request per season.
	No real use of class names or ids... Need to get all <p> tags I guess 
	
	'''
	summaries = []
	for season in range(1,8):
		r = requests.get('http://www.chosentwo.com/buffy/episodes/summaries%i.php' % season)
		page = r.text
		soup = BeautifulSoup(page, 'lxml')
		table = soup.find('table',{'cellspacing':'4'})
		
		
		ptags = table.findAll('p')
		for ptag in ptags:
			ptag.a.decompose()
			ptag.b.decompose()
			summary = ptag.getText()
			summary = summary.replace('\n'," ").replace('\r', " ") # remove extra line breaks
			sentences = summary.split('.')
			trimmed_sentences = []
			for i in range(len(sentences)):
				sentence = sentences[i]
				if not ( ('directed' in sentence.lower()) or ('also star' in sentence.lower() )):
					if len(sentence) > 8:
						trimmed_sentences.append(sentence)
			summary = '.'.join(trimmed_sentences) + "."
			# remove text before hyphens
			if (' - ' in summary):
				summary = ''.join(summary.split( " - ")[1:])
			if (' -- ' in summary):
				summary = ''.join(summary.split( " -- ")[1:])
			#remove text in parentheses
			summary = re.sub("[\(\[].*?[\)\]]", "", summary)
			
			
			summaries.append(summary)
		
		print("chosentwo.com: Found %i episodes in season %i." % (len(ptags), season))
	print("chosentwo.com: found %i summaries total." % len(summaries))
	return (summaries)