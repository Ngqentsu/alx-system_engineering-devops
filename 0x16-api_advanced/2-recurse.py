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
    params = {'after': after,
              'limit': 100}

    if response.status_code != 200:
        return None
    data = response.json().get('data')
    articles = data.get('children')
    for a in articles:
        hot_list.append(a.get('title'))
        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
