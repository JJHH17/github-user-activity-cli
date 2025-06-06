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

    get_user_events(user_input, int(page_count))

# TODO: Add error handling for incorrect address, page numbers
# TODO: Handle time and date formatting
# TODO: Allow user to request specific event types