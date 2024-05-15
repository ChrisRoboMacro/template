from APIkeys import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import requests
from requests_oauthlib import OAuth1

def create_headers():
    return {"Content-Type": "application/json"}

def create_data():
    return {"text": "HELLO WORLD"}

def create_tweet(headers, data):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    response = requests.post(url, headers=headers, json=data, auth=auth)
    if response.status_code != 201:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()

headers = create_headers()
data = create_data()
response = create_tweet(headers, data)
print("Tweet posted:", response)



### THIS EXACT CODE WORKS DO NOT FUCK WITH IT:
"""
from APIkeys import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import requests
from requests_oauthlib import OAuth1

def create_headers():
    return {"Content-Type": "application/json"}

def create_data():
    return {"text": "HELLO WORLD"}

def create_tweet(headers, data):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    response = requests.post(url, headers=headers, json=data, auth=auth)
    if response.status_code != 201:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()

headers = create_headers()
data = create_data()
response = create_tweet(headers, data)
print("Tweet posted:", response)
"""