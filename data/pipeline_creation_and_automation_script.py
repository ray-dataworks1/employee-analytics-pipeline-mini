## employee_id, first_name, last_name, department_id, department_name, salary, hire_date, job_title, job_description, location
## 1, Kylie, White, 3, Engineering, 75000, 2020-01-15, Software Engineer, Develops software solutions, London
## 2, Dylan, Smith, 2, Marketing, 60000, 2019-03-22, Marketing Specialist, Manages marketing campaigns, Manchester
## 3, Emma, Johnson, 1, Sales, 80000, 2018-07-30, Sales Manager, Oversees sales team, Birmingham
## 4, Liam, Brown, 3, Engineering, 55000, 2021-05-10, Software Engineer, Develops software solutions, Leeds
## 5, Olivia, Taylor, 4, Human Resources, 70000, 2022-02-18, Resourcing Manager, Handles HR tasks, London


import csv

data = [
    {"employee_id": 1, "first_name": "Kylie", "last_name": "White", "department_id": 3, "department_name": "Engineering", "salary": 75000, "hire_date": "2020-01-15", "job_title": "Software Engineer", "job_description": "Develops software solutions", "location": "London"},
    {"employee_id": 2, "first_name": "Dylan", "last_name": "Smith", "department_id": 2, "department_name": "Marketing", "salary": 60000, "hire_date": "2019-03-22", "job_title": "Marketing Specialist", "job_description": "Manages marketing campaigns", "location": "Manchester"},
    {"employee_id": 3, "first_name": "Emma", "last_name": "Johnson", "department_id": 1, "department_name": "Sales", "salary": 80000, "hire_date": "2018-07-30", "job_title": "Sales Manager", "job_description": "Oversees sales team", "location": "Birmingham"},
    {"employee_id": 4, "first_name": "Liam", "last_name": "Brown", "department_id": 3, "department_name": "Engineering", "salary": 55000, "hire_date": "2021-05-10", "job_title": "Software Engineer", "job_description": "Develops software solutions", "location": "Leeds"},
    {"employee_id": 5, "first_name": "Olivia", "last_name" : "Taylor", "department_id": 4, "department_name": "Human Resources", "salary": 70000, "hire_date": "2022-02-18", "job_title": "Resourcing Manager", "job_description": "Handles HR tasks", "location": "London"}
]

with open('employee_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["employee_id", "first_name", "last_name", "department_id", "department_name", "salary", "hire_date", "job_title", "job_description", "location"])
    writer.writeheader()
    writer.writerows(data)


    print("Employee data has been written to employee_data.csv")