#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""
import requests
from collections import Counter


def count_words(subreddit, word_list):
    """
    Hot posts by subreddit in a recursive way with sorted count
    """
    headers = {"User-Agent": "kyeeh"}
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    counters = Counter()

    while True:
        try:
            response = requests.get(url, headers=headers,
                                    allow_redirects=False).json()
            hot_posts = response["data"]["children"]
            for post in hot_posts:
                title = post["data"]["title"].lower()
                for word in word_list:
                    counters[word] += title.split(' ').count(word.lower())
            if response["data"].get("after"):
                url = "https://api.reddit.com/r/{}/hot?after={}".
                format(subreddit, response["data"]["after"])
            else:
                break
        except Exception:
            return None

    sorted_counters = sorted(counters.items(),
                             key=lambda x: x[1], reverse=True)
    for key, value in sorted_counters:
        if value != 0:
            print('{}: {}'.format(key, value))
