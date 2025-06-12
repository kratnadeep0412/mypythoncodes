# Python Program: Read and Manage Employee Details Using Dictionary
# Step 1: Read employee details and store in a dictionary
num_employees = int(input("Enter the number of employees: "))
employees = {}
for i in range(num_employees):
    print(f"\nEnter details of employee {i+1}:")
    emp_id = input("Employee ID: ")
    name = input("Employee Name: ")
    designation = input("Designation: ")
    salary = float(input("Salary: "))
    dept_number = input("Department Number: ")
    dept_name = input("Department Name: ")
    reporting_manager = input("Reporting Manager: ")

    employees[emp_id] = {
        'Name': name,
        'Designation': designation,
        'Salary': salary,
        'Department Number': dept_number,
        'Department Name': dept_name,
        'Reporting Manager': reporting_manager
    }
# Step 2: Print individual employee details
print("\n--- Individual Employee Details ---")
for emp_id, details in employees.items():
    print(f"\nEmployee ID: {emp_id}")
    for key, value in details.items():
        print(f"{key}: {value}")
# Step 3: Print list of employee names and tuple of salaries
employee_names = [details['Name'] for details in employees.values()]
salaries = tuple(details['Salary'] for details in employees.values())

print("\nList of Employee Names:", employee_names)
print("Tuple of Salaries:", salaries)
# Step 4: Print dictionary of reporting managers
reporting_managers = {emp_id: details['Reporting Manager'] for emp_id, details in employees.items()}
print("\n--- Reporting Managers (Employee ID: Reporting Manager) ---")
print(reporting_managers)
# Step 5: Print department names and department numbers individually
print("\n--- Department Details ---")
for emp_id, details in employees.items():
    print(f"Employee ID: {emp_id} --> Department Number: {details['Department Number']}, Department Name: {details['Department Name']}")
