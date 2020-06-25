portion_down_payment = 0.25

current_savings = 0

r = 0.04 / 12


total_cost = float(input("Total Cost:"))
annual_salary = float(input("Annual Salary:"))
portion_saved = float(input("Portion Saved:"))

monthly_salary = annual_salary / 12


months_taken =0 

while current_savings < (total_cost * portion_down_payment):
    months_taken += 1

    current_savings += current_savings * r

    current_savings += monthly_salary * portion_saved

print(months_taken)