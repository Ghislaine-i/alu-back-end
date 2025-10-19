#!/usr/bin/python3
"""
Python script that returns information about an employee's TODO list progress
using a REST API.
"""
import requests
import sys

if __name__ == "__main__":
    # Check if an employee ID was provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Base URL for the fake REST API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    user_url = f"{base_url}/users/{employee_id}"
    response = requests.get(user_url)
    if response.status_code != 200:
        print("User not found.")
        sys.exit(1)
    employee = response.json()
    employee_name = employee.get("name")

    # Get all todos for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    done_tasks = [task for task in todos if task.get("completed") is True]

    # Display results
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{len(todos)}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

