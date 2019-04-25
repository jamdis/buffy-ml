import os
import googleapiclient.discovery
import apiKeys


# Couldn't scrape YouTube, so using their API here.

# Based upon Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python



def getYouTubeSummaries():
	summaries = []
	playlists = [
		'ELC1UGRvJP9T4',
		'ELOARsV1QT6jg',
		'ELwT1xo4zchfU',
		'ELsiEFW-kOmIQ',
		'ELDne3nanX55g',
		'EL-E0Jwstibe0',
		'ELG1IHAW8zWC0'
	]
	
	for playlist in playlists:
		summaries.extend(getPlaylistSummaries(playlist))
	print("Youtube: Found a total of %i summaries." % len(summaries))
	return summaries
	
def getPlaylistSummaries(playlist_id):
	summaries = []
	# Disable OAuthlib's HTTPS verification when running locally.
	# *DO NOT* leave this option enabled in production.
	os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

	api_service_name = "youtube"
	api_version = "v3"
	DEVELOPER_KEY = apiKeys.youtube_key

	youtube = googleapiclient.discovery.build(
		api_service_name, api_version, developerKey = DEVELOPER_KEY)

	request = youtube.playlistItems().list(
		part="snippet,contentDetails",
		maxResults=25,
		playlistId=playlist_id
	)
	response = request.execute()
	for item in response['items']:
		summaries.append( (item['snippet']['description']) )
	print ("Youtube: found %s summaries" % len(summaries))
	return summaries