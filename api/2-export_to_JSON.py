#!/usr/bin/python3
"""
Exports data in JSON format for a given employee ID.
"""

import json
import requests
import sys


if __name__ == "__main__":
    # Check if employee ID is passed as argument
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user and tasks
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Failed to retrieve data from the API.")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get("username")

    # Prepare JSON structure
    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {employee_id: tasks}

    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)


