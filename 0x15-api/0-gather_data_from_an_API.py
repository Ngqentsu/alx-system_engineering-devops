#!/usr/bin/python3
"""
Python script that uses REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    employee_id = int(sys.argv[1])
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    user_response = requests.get(users_url + f'/{employee_id}')

    todos = todos_response.json()
    user = user_response.json()

    completed = []

    for task in todos:
        if task.get("completed"):
            completed.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for i in completed:
        print("\t{}".format(i))
