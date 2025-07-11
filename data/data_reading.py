import csv

with open('C:/Users/rogun/pipeline_automation_mini_project/data/employee_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)