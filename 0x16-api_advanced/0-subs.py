#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers(not active
users, total subscribers) for a given subreddit. if an invalid subreddit
is given, the function should return 0.
"""

import request


def number_of_subscribers(subreddit):
    # Defines the base URL for the Reddit API
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Define custom User-Agent to avoid Too Many Requests errors
    headers = {
            "User agent" = "0x16. API_advanced-vinsky001"
            }

    # Send a GET request to the API
    response = requests.get(base_url, headers=headers, allow_redirects=False)
    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the number of subscribers from the JSON data
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
