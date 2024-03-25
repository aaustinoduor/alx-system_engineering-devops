#!/usr/bin/python3
"""Exports to-do list information for given employee ID to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    # get user ID from command-line arguments provided to script
    user_id = sys.argv[1]

    # define base URL for JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # fetch user information from API and
    #   convert response to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # extract username from user data
    username = user.get("username")

    # fetch to-do list items associated with the
    #   given user ID and convert the response to a JSON object
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # use list comprehension for iteration over the to-do list items
    # Write each item's details (user ID, username, completion status,
    #   and title) in a row in the CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
