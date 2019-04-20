import requests


#create a textfile, erasing the old one if it existss
open("buffy-summaries.txt", "w+").close()

def addSummary(summary):
	print("adding %s!" % summary)
	f = open("buffy-summaries.txt", "a+")
	f.write(summary + "\r\n|\r\n")
	f.close



