ename=input("Enter The Name:")
eid=input("Enter The EmpID:")
esal=float(input("Enter Basic Monthly Salary:"))
eallow=float(input("Enter Special Allowances (Monthly): "))
ebonuspercent=float((input("Bonus Percentage (Annual Bonus as % of Gross Salary):")))
gross_monthly_salary=esal+eallow
annual_gross_salary = (gross_monthly_salary * 12) + ((gross_monthly_salary * 12) * int(ebonuspercent) / 100)
print("\n----- Employee Details -----")
print(f"Name: {ename}")
print(f"EmpID: {eid}")
print(f"Basic Monthly Salary: {esal}")
print(f"Special Allowances : {eallow}")
print(f"Gross Monthly Salary: {gross_monthly_salary}")
print(f"Annual Gross Salary (including Bonus): {annual_gross_salary}")
standard_deduction = 50000
if annual_gross_salary > standard_deduction  :
    taxableincome = annual_gross_salary-float(standard_deduction) 
    print(f"Standard_deduction : {standard_deduction }")
    print(f"Taxable Income : {taxableincome}")