hourlyWage = float(input("Enter the hourly wage: "))
regularHours = float(input("Enter the total regular hours: "))
overtimeHours = float(input("Enter the total overtime hours: "))

overtimePay = overtimeHours * 1.5 * hourlyWage
totalPay = (hourlyWage * regularHours) + overtimePay

print("Total weekly pay is: ", totalPay)
