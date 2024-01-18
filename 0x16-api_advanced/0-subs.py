#!/usr/bin/python3
"""
A function that queries the Reddit API and
returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """Function to query subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        results = response.json()
        subscribers = results['data']['subscribers']
        return subscribers
