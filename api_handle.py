# File responsible for API authentication and fetching methods

import requests
import json

username = "JJHH17"
base_url = f"https://api.github.com/users"
return_quantity = 10 # To be made dynamic via user input

def get_user_events(username):
    url = f"{base_url}/{username}/events?per_page={return_quantity}"
    response = requests.get(url)

    if response.status_code == 200:
        events = response.json()
        for event in events:
            print(f"- Type: {event['type']} | Repository: {event['repo']['name']} | Date: {event['created_at']}")
    else:
        print("Something went wrong")
