import requests

API_URL = "https://api.leocrapart.com"

def getRoot():
	res = requests.get(API_URL)
	return res.json()


def getAllWords():
	res = requests.get(f"{API_URL}/words")
	return res.json()

def insertWord(word):
	wordItem = {"word": word}
	res = requests.post(f"{API_URL}/words", json = wordItem)
	return res.json()

def deleteWord(word):
	res = requests.delete(f"{API_URL}/words/{word}")
	return res.json()