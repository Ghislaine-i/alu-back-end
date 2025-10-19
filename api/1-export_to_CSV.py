#!/usr/bin/python3
"""
Script that exports an employee's TODO list to a CSV file.
Usage: python3 1-export_to_CSV.py <employee_id>
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # API base URL
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_resp = requests.get(f"{base_url}/users/{employee_id}")
    if user_resp.status_code != 200:
        print("User not found.")
        sys.exit(1)
    user = user_resp.json()
    username = user.get("username")

    # Fetch all todos for this user
    todos_resp = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos = todos_resp.json()

    # Prepare CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

    print(f"Data exported to {csv_filename}")

