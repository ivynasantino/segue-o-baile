__author__ = "Ivyna Santino"

import requests

#importar do auth.py
URL = ""
API_KEY = ""

def url(method, user, search_name):
	return URL + method + "=" + user + "&artist=" + search_name + "&api_key=" + API_KEY + "&format=json"

def url(method, user):
	return URL + method + "=" + user + "&api_key=" + API_KEY + "&format=json"


def get_artist_tracks_user(user, artist):
	url_requests = url("user.getartisttracks&user", user, artist)
	return requests.get(url_requests).content
	
def get_love_tracks_user(user):
	url_requests = url("user.getlovedtracks&user", user)
	return requests.get(url_requests).content
	
def get_recent_tracks_user(user):
	url_requests = url("user.getrecenttracks&user", user)
	return requests.get(url_requests).content
	
def get_top_album_user(user):
	url_requests = url("user.gettopalbums&user", user)
	return requests.get(url_requests).content

def get_top_artist_user(user):
	url_requests = url("user.gettopartist$user", user)
	return requests.get(url_requests).content

def get_top_tags_user(user):
	url_requests = url("user.gettoptags$user", user)
	return requests.get(url_requests).content

def get_top_tracks_user(user):
	url_requests = url("user.gettoptracks$user", user)
	return requests.get(url_requests).content
