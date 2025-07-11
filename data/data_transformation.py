import csv

filtered = []

with open('C:/Users/rogun/pipeline_automation_mini_project/data/employee_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['salary']) > 60000 and row['location'] == 'London':
            filtered.append(row)

with open('C:/Users/rogun/pipeline_automation_mini_project/data/employee_over_60k_london_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["employee_id", "first_name", "last_name", "department_id", "department_name", "salary", "hire_date", "job_title", "job_description", "location"])
    writer.writeheader()
    writer.writerows(filtered)



print("Filtered employee data has been written to employee_over_60k_london_data.csv!")