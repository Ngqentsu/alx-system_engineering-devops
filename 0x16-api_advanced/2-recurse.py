#!/usr/bin/python3
"""Recursive function that queries the Reddit API and
   returns list containing the titles of all hot articles
   for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """Returns list with titles of all hot articles for given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    params = {'limit': 100
              'after': after
              'count': count}

    if response.status_code == 200:
        data = response.json().get('data')
        return data.get('subscribers')
    else:
        return 0
