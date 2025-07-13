import csv

def write_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['employee_id', 'first_name', 'last_name', 'department_id', 'department_name', 'salary', 'hire_date', 'job_title', 'job_description', 'location'])
        writer.writeheader()
        writer.writerows(data)
        print(f"Data has been written to {filename}")

def read_and_filter(input_file, output_file):
    filtered = []
    with open(input_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['salary']) > 60000 and row['location'] == 'London':
                filtered.append(row)
    write_csv(filtered, output_file)


if __name__ == "__main__":
    # 1. Make a CSV file
    data = [
        {"employee_id": 1, "first_name": "Kylie", "last_name" : "White", "department_id": 3, "department_name": "Engineering", "salary": 75000, "hire_date": "2020-01-15", "job_title": "Software Engineer", "job_description": "Develops software solutions", "location": "London"},
        {"employee_id": 2, "first_name": "Dylan", "last_name" : "Smith", "department_id": 2, "department_name": "Marketing", "salary": 60000, "hire_date": "2019-03-22", "job_title": "Marketing Specialist", "job_description": "Manages marketing campaigns", "location": "Manchester"},
        {"employee_id": 3, "first_name": "Emma", "last_name" : "Johnson", "department_id": 1, "department_name": "Sales", "salary": 80000, "hire_date": "2018-07-30", "job_title": "Sales Manager", "job_description": "Oversees sales team", "location": "Birmingham"},
        {"employee_id": 4, "first_name": "Liam", "last_name": "Brown", "department_id": 3, "department_name": "Engineering", "salary": 55000, "hire_date": "2021-05-10", "job_title": "Software Engineer", "job_description": "Develops software solutions", "location": "Leeds"},
        {"employee_id": 5, "first_name": "Olivia", "last_name": "Taylor", "department_id": 4, "department_name": "Human Resources", "salary": 70000, "hire_date": "2022-02-18", "job_title": "Resourcing Manager", "job_description": "Handles HR tasks", "location": "London"}
    ]
    write_csv(data, 'employee_data.csv')

    read_and_filter('employee_data.csv', 'employee_over_60k_london_data.csv')
    print("Full pipeline and automation script executed successfully! Check the output files.")

from datetime import datetime
with open("pipeline_run.log", "a") as log:
    log.write(f"Pipeline ran at {datetime.now()}\n")
