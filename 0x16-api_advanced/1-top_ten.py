#!/usr/bin/python3
"""
Script to print hot posts on a particular Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """Print titles of the 10 hottest posts on a given subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit=10'.format(
        subreddit)
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16)'}
    response = requests.get(url, headers=headers)
    try:
        top_ten = response.json()['data']['children']
        for post in top_ten:
            print(post['data']['title'])
    except KeyError:
        print("None")
