#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """Function to query subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    subscribers_count = results.get("subscribers")
    return subscribers_count
