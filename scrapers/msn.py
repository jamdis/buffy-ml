import requests
import re
import sneakyrequest

def getMsnSummaries():
	'''
	Get plot summaries from msn.com.
	'''
	headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
	r = requests.get('https://www.msn.com/en-us/entertainment/rf-watch-online/tv-shows/buffy-the-vampire-slayer-1997/season-1/', headers = headers)
	print(r)
	#page = r.text
	
	with open('msn.html', 'w+') as f:
				f.write(r.text)
	