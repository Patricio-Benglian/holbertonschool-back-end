#!/usr/bin/python3
"""Export to JSON module"""
import requests
from sys import argv
import json

if __name__ == "__main__":
    employee_id = argv[1]  # Usage: ./filename {id}
    task_list = []  # Will hold info on each task

    # Fetch info
    employee = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    # Add tasks to list
    for task in employee_todos.json():
        task_dict = {"task": task["title"], "completed": task["completed"],
                     "username": employee.json()["username"]}
        task_list.append(task_dict)

    # Create dict with ID as Key and list as Value
    employee_task_dict = {f"{employee_id}": task_list}

    with open(f'{argv[1]}.json', 'w', encoding='utf-8') as file:
        json.dump(employee_task_dict, file)
