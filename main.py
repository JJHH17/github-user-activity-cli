# File responsible for main functions of tool

import requests
import json
from api_handle import get_user_events

# Used to gather user input
while True:
    user_input = input("Please enter your GitHub username: ")

    if user_input == "Exit" or user_input == "exit":
        break

    page_count = input("Please enter how many events you want to return: ")

    if page_count == "Exit" or page_count == "exit":
        break

    # Handling page count errors
    try:
        # Pagination limit check
        if int(page_count) > 33:
            get_user_events(user_input, 33)
            print("This service is limited to 33 responses.")

        else:
            get_user_events(user_input, int(page_count))

    except ValueError as ve:
        print("Please enter a valid number.")


# TODO: Handle time and date formatting
# TODO: Allow user to request specific event types