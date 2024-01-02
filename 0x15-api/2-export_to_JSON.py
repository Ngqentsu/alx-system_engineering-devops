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

    employee_id = int(sys.argv[1])
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    user_response = requests.get(users_url + f'/{employee_id}')

    todos = todos_response.json()
    user = user_response.json()

    user_id = user.get('id')
    username = user.get('username')

    json_filename = f'{user_id}.json'
    json_data = {str(user_id): []}

    for task in todos:
        json_data[str(user_id)].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })

    with open(json_filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)
