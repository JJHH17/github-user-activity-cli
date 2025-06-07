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
    new_time = new_time[len(new_time) // 2:] # Slices response to get time
    new_time = new_time[1:-1] # Cuts start and end of string for better formatting
    return new_time


def get_user_events(username, page_count):
    url = f"{base_url}/{username}/events?per_page={page_count}"
    response = requests.get(url)

    if response.status_code == 200:
        events = response.json()

        # Handling null instances
        if len(events) == 0:
            print("\nNo activity found")

        else:
            for event in events:
                print(f"- Type: {event['type']} | Repository: {event['repo']['name']} | Date: {date_convert(event)} | Time: {time_convert(event)}")

    # Handles timeout
    elif response.status_code == 408:
        print("\nYour request timed out, please try again later.")

    # Handles unrecognised credentials
    elif response.status_code == 404:
        print(f"\nUsername {username} or resource not found, please try again!")

    elif response.status_code == 503:
        print("\nService temporarily unavailable - Please try again later.")