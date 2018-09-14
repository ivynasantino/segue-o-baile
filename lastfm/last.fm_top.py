__author__ = "Ivyna Santino"

import requests

URL = ""
API_KEY = ""

def url(method, search_name):
	return URL + method + search_name + "&api_key=" + API_KEY + "&format=json"


def get_top_tag_artist(disco):
	url_request = url("tag.gettopartists&tag=", disco)
	return requests.get(url_request).content
	
def get_top_album_artist(artist):
	url_request = url("artist.gettopalbums&artist=", artist)
	return request.get(url_request).content
	
