__author__ = "Ivyna Santino"

import requests

#importar do auth.py
URL = ""
API_KEY = ""

def url(method, artist, album):
	return URL + method + "&api_key=" + API_KEY + "&artist=" + artist + "&album=" + album + "&format=json"

def url_2(method, artist, album):
	return URL + method + "&artist=" + artist + "&album=" + album + "&api_key=" + API_KEY + "&format=json"


def get_info_album(artist, album):
	url_request = url("album.getinfo", artist, album)
	return requests.get(url_request).content

def get_tags_album(artist, album):
	url_request = url_2("album.gettags", artist, album)
	return requests.get(url_request).content
