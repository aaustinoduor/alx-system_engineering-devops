#!/usr/bin/python3
"""
script which queries subscribers on a particular Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """return total number of subscribers on a particular subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 300:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
