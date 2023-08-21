#!/usr/bin/python3
"""Export to JSON module"""
import json
import requests

if __name__ == "__main__":
    employees_dict = {}  # Will have ID: [list_of_tasks]

    # Fetch info
    employees = requests.get(
        f"https://jsonplaceholder.typicode.com/users/")
    employee_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos")

    for employee in employees.json():
        employee_task_list = []
        for task in employee_todos.json():
            if task['userId'] == employee['id']:
                task_dict = {"username": employee['username'],
                             "task": task['title'],
                             "completed": task['completed']}
                employee_task_list.append(task_dict)
        employees_dict[employee['id']] = employee_task_list

    with open(f'todo_all_employees.json', 'w', encoding='utf-8') as file:
        json.dump(employees_dict, file)
