import apiKeys
import requests
import json

def getOMDBSummaries():
	'''
	Gets plots from OBMD API of imdb info. 
	Some episodes are not coming up with this method, and others are truncated.
	May go back and scrape IMDB after all?
	'''	
	summaries = []
	
	for i in range (1,8):
		for j in range(1,23):
			if i == 1 and j > 12:
				pass
			else:
				payload = {'apikey' : apiKeys.omdb_key, 'season' : i, 'episode' : j}
				r = requests.get("http://www.omdbapi.com/?t=Buffy%20The%20Vampire%20Slayer&plot=full", params = payload)
				json_results = json.loads(r.text)
				
				print("OMDB: getting Season %i Episode %i" % (i, j))
				try:
					summary = json_results['Plot']
					if summary.endswith("..."):
						print("OMDB -- S%iE%i summary truncated with '...':" % (i,j))
					else:
						summaries.append(summary)
				except KeyError:
					print("OMDB -- no plot data for S%iE%i Here's the JSON:" % (i,j))
					print(r.text)
				except:
					raise
	return summaries