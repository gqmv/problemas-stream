def calculate_savings(rate, semi_annual_raise, monthly_salary, months_taken, portion_saved):
    savings = 0
    
    current_sallary = monthly_salary

    for month in range(1, months_taken + 1):
        savings *= 1 + rate
        savings += current_sallary * portion_saved

        if month % 6 == 0:
            current_sallary *= 1 + semi_annual_raise
            
    return savings


semi_annual_raise = 0.07

portion_down_payment = 0.25

r = 0.04 / 12

total_cost = 1000000

ERROR_RATE = 100

months_taken = 36


annual_salary = float(input("Annual Salary:"))

monthly_salary = annual_salary / 12

savings = 0
max_value = 1
min_value = 0
value = 0

if calculate_savings(r, semi_annual_raise, monthly_salary, months_taken, 1) < total_cost * portion_down_payment:
    print("Not possible")
else:

    indicador = False
    while abs(total_cost * portion_down_payment - savings) > 100:
        if not indicador:
            indicador = True
        value = (max_value + min_value) / 2
        savings = calculate_savings(r, semi_annual_raise, monthly_salary, months_taken, value)

        if savings > total_cost * portion_down_payment:
            max_value = value
        else:
            min_value = value

    print(value)
