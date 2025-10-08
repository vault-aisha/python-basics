def calculate_savings_growth(savings, rate):
    interest = savings * rate
    total_amount = savings + interest
    return total_amount

savings = float(input("Enter your savings amount: "))
rate = float(input("Enter interest rate: "))

print("Your total savings is {:.2f}".format(calculate_savings_growth(savings, rate)))
