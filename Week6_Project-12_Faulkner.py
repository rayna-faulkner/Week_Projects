def payroll_report(emp_info):
    print("Employee Payroll Report")
    print("-----------------------")
    print("Last Name\tHours Worked\tWages Paid")
    print("------------------------------------")
    for emp in emp_info:
        last_name, hourly_wage = emp
        hours_worked = float(input(f"Enter hours worked for {last_name}: "))
        wages_paid = hourly_wage * hours_worked
        print(f"{last_name}\t\t{hours_worked}\t\t{wages_paid:.2f}")


filename = input("Enter the filename: ")

emp_info = []

generate_payroll_report(emp_info)
