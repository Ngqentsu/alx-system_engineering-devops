#!/usr/bin/python3
"""Function that queries the Reddit API and
   returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a subredit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        return 0
    data = response.json().get('data')
    return data.get('subscribers')
