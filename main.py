import requests  # if you don't have this installed by default, run: pip install requests

def send_to_discord(webhook_url, message):  # function definition
    data = {  # JSON variable with data stored
        "content": message,  # correct the key from "contnet" to "content"
        "username": "YoutubeTutorial"
    }

    result = requests.post(webhook_url, json=data)  # post request to webhook URL

    try:
        result.raise_for_status()  # check for HTTP errors
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
    else:
        print(f"Success: {result.status_code}")

webhook_url = '#add webhook link here'  # replace with your webhook URL
message = 'example message'
send_to_discord(webhook_url, message)
