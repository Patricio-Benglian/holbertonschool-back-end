#!/usr/bin/python3
"""gather data module"""
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]  # Usage: ./filename {id}

    # Fetch info
    employee = (requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"))
    employee_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    employee_username = employee.json()['username']
    # Write to CSV
    with open(f'{argv[1]}.csv', 'w') as file:
        for task in employee_todos.json():
            file.write(f'"{employee_id}","{employee_username}"'
                       f',"{task["""completed"""]}","{task["""title"""]}"\n')
