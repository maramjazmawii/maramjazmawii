PERCENT_DIVISOR = 100
DECIMAL_PLACES = 2

bill_amount = float(input("Enter the bill: "))
tip_percentage = int(input("Enter tip percent: "))
number_of_diners = int(input("Enter number of diners: "))

tip_amount = bill_amount * (tip_percentage / PERCENT_DIVISOR)
total_amount = bill_amount + tip_amount
price_per_diner = total_amount / number_of_diners

print(f"Tip: {tip_amount:.{DECIMAL_PLACES}f}")
print(f"Total: {total_amount:.{DECIMAL_PLACES}f}")
print(f"Each person pays: {price_per_diner:.{DECIMAL_PLACES}f}")
