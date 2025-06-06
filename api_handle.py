# File responsible for API authentication and fetching methods

import requests
import json

base_url = f"https://api.github.com/users"

def get_user_events(username, page_count):
    url = f"{base_url}/{username}/events?per_page={page_count}"
    response = requests.get(url)

    if response.status_code == 200:
        events = response.json()
        for event in events:
            print(f"- Type: {event['type']} | Repository: {event['repo']['name']} | Date: {event['created_at']}")

    # Handles unrecognised credentials
    elif response.status_code == 404:
        print(f"Username {username} not found, please try again!")
