#!/usr/bin/python3
"""Function that queries the Reddit API and
   returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a subredit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'u/Organic-Programmer72'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data')
        return data.get('subscribers', 0)
    else:
        return 0
