__author__ = "Ivyna Santino"

import requests

URL = ""
API_KEY = ""

def url(method, artist, search_track):
	return URL + method + "&artist=" + artist + "&track=" + search_track + "&api_key=" + API_KEY + "&format=json"

def url(method, artist, user, search_track):
	return URL + method + "&api_key=" + API_KEY + "&artist=" + artist + "&track=" + search_track + "&user=" + user + "&format=json"
	

def get_correction_track(artist, track):
	url_requests = url("track.getcorrection", artist, track)
	return requests.get(url_requests).content
	
def get_similar_track(artist, track):
	url_requests = url("track.getSimilar", artist, track)
	return requests.get(url_requests).content
	
def get_tags_track(artist, track):
	url_requests = url("track.getTags", artist, user, track)
	return requests.get(url_requests).content
