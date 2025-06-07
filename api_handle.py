# File responsible for API authentication and fetching methods

import requests
import json

base_url = f"https://api.github.com/users"


# Handles displaying date of event
def date_convert(input):
    new_date = input["created_at"]
    new_date = new_date[:len(new_date) // 2] # Slices response in half to only grab the date
    return new_date


# Handles displaying time of event
def time_convert(input):
    new_time = input["created_at"]


def get_user_events(username, page_count):
    url = f"{base_url}/{username}/events?per_page={page_count}"
    response = requests.get(url)

    if response.status_code == 200:
        events = response.json()
        for event in events:
            print(f"- Type: {event['type']} | Repository: {event['repo']['name']} | Date: {date_convert(event)}")

    # Handles unrecognised credentials
    elif response.status_code == 404:
        print(f"Username {username} not found, please try again!")
