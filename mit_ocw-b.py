current_savings = 0

portion_down_payment = 0.25

r = 0.04 / 12


total_cost = float(input("Total Cost:"))
annual_salary = float(input("Annual Salary:"))
portion_saved = float(input("Portion Saved:"))
semi_annual_raise = float(input("Semi-annual-raise:"))

monthly_salary = annual_salary / 12


months_taken =0 

while current_savings < (total_cost * portion_down_payment):
    months_taken += 1

    current_savings += current_savings * r

    current_savings += monthly_salary * portion_saved

    if months_taken % 6 == 0:
        monthly_salary *= 1 + semi_annual_raise

print(months_taken)