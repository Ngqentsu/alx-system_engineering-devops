#!/usr/bin/python3
"""Function that queries the Reddit API, parses the title of
   all hot articles, and prints a sorted count of
   given keywords, delimited by spaces
"""

import requests
from collections import Counter

def count_words(subreddit, word_list, after=None, counts=None):
    """Recursive function to count occurrences of keywords in hot articles."""
    if counts is None:
        counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    posts = results.get("children")

    for post in posts:
        title = post.get("data").get("title")
        title_lower = title.lower()

        for word in word_list:
            word_lower = word.lower()
            if word_lower in title_lower:
                counts[word_lower] += 1

    after = results.get("after")
    if after:
        count_words(subreddit, word_list, after, counts)

    sorted_counts = sorted(counts.items(),
                           key=lambda x: (-x[1], x[0]))
    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")
