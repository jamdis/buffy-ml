import requests
import apiKeys
import json
from bs4 import BeautifulSoup
import time
import random
import re
import scrapers
from sneakyrequest import sneakyRequest

#create a textfile, erasing the old one if it exists
open("buffy-summaries.txt", "w+").close()

def addSummary(summary):
	summary = summary.strip()
	f = open("buffy-summaries.txt", "a+")
	f.write(summary + "\r\n|\r\n")
	f.close

def addSummaries(summaries):
	for summary in summaries:
		addSummary(summary)
		

def getAllSummaries():
	#addSummaries(scrapers.getOMDBSummaries())
	#addSummaries(scrapers.getWikipediaSummaries())
	#addSummaries(scrapers.getTvDotComSummaries())
	#addSummaries(scrapers.getITunesSummaries())
	#addSummaries(scrapers.getHuluSummaries())
	#addSummaries(scrapers.getYouTubeSummaries())
	scrapers.getWatchOnlineSummaries()
	
	#addSummaries(scrapers.getAmazonSummaries())
getAllSummaries()