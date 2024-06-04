#!/usr/bin/python3
"""Recursive function that queries the Reddit API and
   returns list containing the titles of all hot articles
   for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """Returns list with titles of all hot articles for given subreddit"""
    if hot_list is None:
        hot_list = []
    if after is None:
        after = ''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    params = {'after': after,
              'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None
    data = response.json().get('data')
    after = data.get('after')
    articles = data.get('children')
    for a in articles:
        hot_list.append(a.get('data').get('title'))
        if after:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
