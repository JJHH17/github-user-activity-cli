# File responsible for main functions of tool

import requests
import json
from api_handle import get_user_events

# get_user_events(username)

# Loop for program functionality
flag = True

# Used to gather user input
while flag:
    user_input = input("Please enter your GitHub username: ")
    page_count = int(input("Please enter how many events you want to return: "))
    if user_input == "Exit" or "exit" or page_count == "Exit" or "exit":
        flag = False

    get_user_events(user_input,page_count)