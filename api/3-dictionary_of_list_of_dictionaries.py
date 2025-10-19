#!/usr/bin/python3
"""
Exports all employees' TODO list data in JSON format.
"""

import json
import requests


if __name__ == "__main__":
    # Base URLs for API endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users and tasks
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Create a dictionary to hold all user data
    all_tasks = {}

    # Loop through each user and collect their tasks
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Filter tasks for this specific user
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]

        # Add to the main dictionary
        all_tasks[user_id] = user_tasks

    # Write all user data to a single JSON file
    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump(all_tasks, jsonfile)

