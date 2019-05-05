import requests
import re
from bs4 import BeautifulSoup
import time

def getBbcAdactioSummaries():
	'''
	This weird old BBC page has weird short summaries on the season pages.
	
	Each episode also has its own page which has a separate weird short summary.
	'''
	summaries = []
	episode_links = []
	
	
	#Season 1 -- this one has different html to the others :/
	print ("BBC Adactio: Getting Season 1")
	r = requests.get('http://bbc.adactio.com/cult/buffy/indetail/season1.shtml')
	page = r.text
	soup = BeautifulSoup(page,'html.parser')
	
	options = soup.findAll('option')
	for option in options:
		episode_links.append(option['value'])
		
	list = soup.find('font',{'face':'Verdana, ARIAL, HELVETICA'})
	list_html = str(list)
	episodes = re.findall("</a><br/>[\s]*[A-Z].*",list_html)
	for episode in episodes:
		summaries.append( BeautifulSoup(episode,'html.parser').get_text().strip()	)	
	#summaries.extend(episodes)
	
	
	for season in range (2,8):
		r = requests.get('http://bbc.adactio.com/cult/buffy/indetail/season%i.shtml' % season)
		print ("BBC Adactio: Getting Season %i" % season)
		time.sleep(2)
		page = r.text
		
		episodes = re.findall("</A></B><BR>.*[A-Z].*",page)
		for episode in episodes:
			summaries.append( BeautifulSoup(episode,'html.parser').get_text().strip()	)
	print ("BBC Adactio: Getting individual episode pages:")
	
	for episode_link in episode_links:
		r = requests.get('http://bbc.adactio.com%s' % episode_link)
		print ("BBC Adactio: Getting %s" % episode_link)
		time.sleep(2)
		page = r.text
		soup = BeautifulSoup(page,'html.parser')
		summary = soup.find('strong')
		if summary is not None:
			summaries.append(summary.get_text())
	
	print ("BBC Adactio: Got %i summaries" % len(summaries))
	
	return (summaries)