#!/usr/bin/python3
"""
Exports to-do list information for given employee ID to JSON format.

this script takes employee ID as command-line argument and exports
the corresponding user information and to-do list to JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    # get employee ID from command-line argument
    user_id = sys.argv[1]

    # base URL for JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # fetch user information using provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # fetch to-do list for employee using provided employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # create dictionary containing user and to-do list information
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # write data to JSON file with employee ID as filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
