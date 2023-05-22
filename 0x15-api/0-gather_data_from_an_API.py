
#!/usr/bin/python3 

"""this code checks for employees todo list and if it has beeen achieved"""

import requests

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get employee information
    employee_response = requests.get(f'{base_url}/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Get employee's TODO list
    todo_response = requests.get(f'{base_url}/todos', params={'userId': employee_id})
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task['completed']]
    num_done_tasks = len(done_tasks)

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

