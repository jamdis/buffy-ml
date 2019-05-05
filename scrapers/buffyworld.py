import requests
import re
import sneakyrequest
from bs4 import BeautifulSoup
import time
import lxml

def getBuffyWorldSummaries():
	'''
	
	
	'''
	summaries = []
	
	
	for i in range (1,145):
		print("Buffy World: %i" %i)
		r = requests.get('http://www.buffyworld.com/buffy/summaries/%s_summ.html' % str(i).zfill(3))
		page  = r.text
		
		soup = BeautifulSoup(page,'lxml')
		summary = soup.find('td')
		paras = summary.find_all('p')
		if(len(paras) == 0):
			paras = summary.get_text().splitlines()
			for para in paras:
				if len(para) > 8:
					summaries.append(para)
		else:
			for para in paras:
				summary = para.get_text().replace('\n', ' ').replace('\r', '')
				summaries.append(summary)
		

		
		
		
	return summaries