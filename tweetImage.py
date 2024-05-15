from APIkeys import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import requests
from requests_oauthlib import OAuth1

def create_headers():
    return {"Content-Type": "application/json"}

def upload_image(file_path):
    url = "https://upload.twitter.com/1.1/media/upload.json"
    auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    files = {'media': open(file_path, 'rb')}
    response = requests.post(url, files=files, auth=auth)
    if response.status_code != 200:
        raise Exception(f"Image upload failed: {response.status_code} {response.text}")
    return response.json()['media_id_string']

def create_tweet(headers, data):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    response = requests.post(url, headers=headers, json=data, auth=auth)
    if response.status_code != 201:
        raise Exception(f"Tweet creation failed: {response.status_code} {response.text}")
    return response.json()

image_path = "chart1.jpg"  # Replace with your image path
media_id = upload_image(image_path)

headers = create_headers()
data = {"text": "HELLO WORLD", "media": {"media_ids": [media_id]}}
response = create_tweet(headers, data)
print("Tweet posted:", response)
