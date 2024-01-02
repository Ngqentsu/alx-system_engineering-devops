#!/usr/bin/python3
"""
Python script that uses REST API,
for a given employee ID, returns information
about his/her TODO list progress and exports data in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    todos_response = requests.get(todos_url)
    users_response = requests.get(users_url)

    todos = todos_response.json()
    users = users_response.json()

    json_data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        json_data[str(user_id)] = []

        for task in todos:
            if task["userId"] == user_id:
                json_data[str(user_id)].append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

    json_filename = 'todo_all_employees.json'

    with open(json_filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)
