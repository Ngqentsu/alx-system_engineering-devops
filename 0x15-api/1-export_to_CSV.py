#!/usr/bin/python3
"""
Python script that uses REST API,
for a given employee ID, returns information
about his/her TODO list progress and exports data in CSV format.
"""

import csv
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

    csv_filename = f'{user_id}.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos:
            csv_writer.writerow([user_id, username,
                                 task["completed"], task["title"]])
