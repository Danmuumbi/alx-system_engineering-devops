#!/usr/bin/python3
'''
gather employee data from API
'''

import sys
import requests

REST_API = "https://jsonplaceholder.typicode.com"

def get_employee_todo_progress(employee_id):
    # Fetch employee data
    employee_data = requests.get(f"{REST_API}/users/{employee_id}").json()
    employee_name = employee_data.get('name')

    # Fetch tasks data
    tasks_data = requests.get(f"{REST_API}/todos").json()

    # Filter tasks for the given employee
    employee_tasks = [task for task in tasks_data if task.get('userId') == employee_id]
    
    # Count completed tasks
    completed_tasks = sum(1 for task in employee_tasks if task.get('completed'))
    
    # Display progress
    total_tasks = len(employee_tasks)
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Display completed tasks
    for task in employee_tasks:
        if task.get('completed'):
            print(f"\t{task.get('title')}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
