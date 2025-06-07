# File responsible for main functions of tool

import requests
import json
from api_handle import get_user_events

# Used to gather user input
while True:
    user_input = input("\nPlease enter your GitHub username: ")

    if user_input.lower() == "exit":
        break

    page_count = input("\nPlease enter how many events you want to return: ")

    if page_count.lower() == "exit":
        break

    # Handling page count errors
    try:
        # Pagination limit check
        if int(page_count) > 33:
            get_user_events(user_input, 33)
            print("\nThis service is limited to 33 responses.")

        else:
            get_user_events(user_input, int(page_count))

    except ValueError as ve:
        print("\nPlease enter a valid number.")

# TODO: Update readme
# TODO: Push and then upload to roadmap.sh