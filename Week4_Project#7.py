beginningSalary = float(input("Enter the starting salary: "))
percentageIncrease = float(input("Enter the percentage increase (in decimal form): "))
yearsNum = int(input("Enter the number of years in the schedule: "))

# Print the header of the salary schedule
print("Year\tSalary")

# Calculate and display the salary schedule
salary = beginningSalary
for year in range(1, yearsNum + 1):
    print(year, "\t$", format(salary, ".2f"))
    salary += salary * percentageIncrease

