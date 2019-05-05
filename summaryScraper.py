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

def cleanSummary(summary):
	re.sub(' +', ' ', summary)
	summary = summary.replace('ï¿½', "'")
	summary = summary.replace('“', '"')
	summary = summary.replace('”', '"')
	summary = summary.replace('ä', 'a')
	summary = summary.replace('\\', '')
	summary = summary.replace('…', '...')
	summary = summary.replace('�', "'")
	summary = summary.replace('\x92', "")
	summary = summary.replace('\xa0', "")
	summary = summary.replace('\x85', "")
	summary = summary.replace('\x97', "")
	summary = summary.replace('\xad', "")
	summary = summary.replace('—', "-")
	summary = summary.replace('-', "-")
	summary = summary.replace('–', "-")
	summary = summary.replace('`', "'")
	summary = summary.replace('’', "'")
	summary = summary.replace('%', " percent")
	summary = summary.replace('*', "")
	summary = summary.replace('+', " plus ")
	summary = summary.replace('[', "")
	summary = summary.replace(']', "")
	summary = summary.replace('_', " ")
	summary = summary.replace('_', " ")
	summary = summary.replace('¹', "")
	summary = summary.replace('Ð', "")
	summary = summary.replace('Ð', "")
	summary = summary.replace('Õ', "'")
	summary = summary.replace('é', "e")
	summary = summary.replace('ü', "u")
	return summary

def addSummary(summary):
	summary = cleanSummary(summary)
	summary = summary.strip()
	f = open("buffy-summaries.txt", "a+")
	f.write(summary + "\r\n|\r\n")
	f.close

def addSummaries(summaries):
	for summary in summaries:
		addSummary(summary)
	
def shuffleSummaries():
	f = open("buffy-summaries.txt", "r+")
	text = f.read()
	f.close()
	summaries = text.split("\r\n|\r\n")
	random.shuffle(summaries)
	text = "\r\n|\r\n".join(summaries)
	f = open("buffy-summaries.txt", "w+")
	f.write(text)
	f.close()

def getAllSummaries():
	addSummaries(scrapers.getOMDBSummaries())
	addSummaries(scrapers.getWikipediaSummaries())
	addSummaries(scrapers.getTvDotComSummaries())
	addSummaries(scrapers.getITunesSummaries())
	addSummaries(scrapers.getHuluSummaries())
	addSummaries(scrapers.getYouTubeSummaries())
	addSummaries(scrapers.getWatchOnlineSummaries())
	addSummaries(scrapers.getBuffyGuideSummaries())
	addSummaries(scrapers.getTvMazeSummaries())
	addSummaries(scrapers.getTvGuideSummaries())
	addSummaries(scrapers.getSimpleWikipediaSummaries())
	addSummaries(scrapers.getRadioTimesSummaries())
	addSummaries(scrapers.getBbcAdactioSummaries())
	addSummaries(scrapers.getVryaSummaries())
	addSummaries(scrapers.getChosenTwoSummaries())
	addSummaries(scrapers.getBtvsOnlineSummaries())
	addSummaries(scrapers.getWikipedia_longSummaries())
	addSummaries(scrapers.getWikiaSummaries())
	addSummaries(scrapers.getBuffyWorldSummaries())
	
	#addSummaries(scrapers.getAmazonSummaries())
	shuffleSummaries()
getAllSummaries()