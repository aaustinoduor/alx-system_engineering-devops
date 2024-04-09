#!/usr/bin/python3
"""
script to print hot posts on a particular Reddit subreddit.
"""

import requests


def top_ten(subreddit):

    # Create URL for subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # define headers for HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # define parameters for request, limiting number of posts to 10
    params = {
        "limit": 10
    }

    # send a GET request to subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # check if response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return

    # parse JSON response and extract 'data' section
    results = response.json().get("data")

    # print titles of top 10 hottest posts
    [print(c.get("data").get("title")) for c in results.get("children")]
