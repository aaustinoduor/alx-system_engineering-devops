#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

this script takes an employee ID as a command-line argument and fetches
corresponding user information and to-do list from JSONPlaceholder API.
It then prints tasks completed by employee.
"""

import requests
import sys


if __name__ == "__main__":
    # base URL for JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # get employee information using provided employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # get to-do list for employee using provided employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # filter completed tasks and count them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # print employee's name and number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # print completed tasks one by one with indentation
    [print("\t {}".format(complete)) for complete in completed]
