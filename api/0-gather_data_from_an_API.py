#!/usr/bin/python3
"""gather data module"""
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]  # Use: ./filename {id}
    complete_tasks = 0
    total_tasks = 0
    complete_list = []

    employee = (requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"))
    employee_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        
    for task in employee_todos.json():
        if task['completed']:
            complete_tasks += 1
            complete_list.append(task)
        total_tasks += 1
    print (f"Employee {employee.json()['name']} is done with tasks({complete_tasks}/{total_tasks}):")
    for task in complete_list:
        print(f"\t {task['title']}")
    

