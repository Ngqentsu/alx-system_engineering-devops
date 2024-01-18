#!/usr/bin/python3
"""Function that returns all hot posts on a given Reddit subreddit."""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """Print the titles of all hottest posts."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 100,
        "after": after
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    
    if response.status_code == 404:
        return None
    
    results = response.json().get("data")
    
    for i in results.get("children"):
        hot_list.append(i.get("data").get("title"))

    after = results.get("after")
    if after:
        recurse(subreddit, hot_list, after)
    
    return hot_list
